from client.wikipedia_api_client import WikipediaApiClient
from datetime import datetime
import os
import argparse
import logging

parser = argparse.ArgumentParser()
parser.add_argument('-W', '--word', type=str, help="Title or search word.")
parser.add_argument('-E', '--exact', action="store_true", help="Search by exact matching")
parser.add_argument('-L', '--limit', type=str, help="Limit of titles.")
args = parser.parse_args()

fmt = '%(asctime)s %(levelname)s [%(module)s#%(funcName)s] :%(message)s'
logging.basicConfig(level=logging.DEBUG, format=fmt)
logger = logging.getLogger('Main')


def write_corpus(corpus):
    """
    Write corpus into a text file.
    :param corpus: a corpus
    """
    base_dir = os.path.dirname(__file__)
    output_dir = os.path.join(base_dir, 'output')
    file_name = 'corpus_{}.txt'.format(datetime.now().strftime("%Y%m%d%H%M%S"))
    file_path = os.path.join(output_dir, file_name)

    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(corpus)


if __name__ == '__main__':
    client = WikipediaApiClient()

    if args.word:
        if args.exact:
            corpus = client.get([args.word])
        else:
            titles = client.search(args.word)
            corpus = client.get(titles)
    else:
        if args.exact:
            raise ValueError("'--word' option is required when '--exact' option exists")
        else:
            logger.info('limit: {}'.format(args.limit))
            titles = client.search_random(limit=args.limit)
            corpus = client.get(titles)

    write_corpus(corpus)
