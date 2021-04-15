# -*- coding: utf-8 -*-
from collections import defaultdict
import os
import json
import requests

def ingest_stories(data_dir: str, col_name: str, url: str):
    response = requests.get(url)
    results: dict = response.json()
    fo_path = os.path.join(data_dir,col_name)+'.json'
    print('ingesting ' + fo_path + '\n from ' + url)
    with open(fo_path, 'w') as fo:
        json.dump(results, fo, indent=1) # save a copy of json result to help with debug
    # TODO: insert into database
    return results

def ingest_node(authors: dict, data_dir: str, node_id: str):
    url = 'https://hacker-news.firebaseio.com/v0/item/{}.json?print=pretty'.format(node_id)
    response = requests.get(url)
    results: dict = response.json()
    # TODO: insert into database instead of creating files
    if 'deleted' not in results:
        authors[results['by']].append(node_id)
        fo_dir = os.path.join(data_dir,node_id)
        os.makedirs(fo_dir, exist_ok=True)
        fo_path = os.path.join(fo_dir,'node.json')
        print('ingesting ' + fo_path + '\n from ' + url)
        with open(fo_path, 'w') as fo:
            json.dump(results, fo, indent=1) # save a copy of json result to help with debug
        if 'kids' in results:
            for kid in results['kids']:
                ingest_node(authors, fo_dir, str(kid))
    return results

def ingest_author(data_dir: str, author_name: str):
    url = 'https://hacker-news.firebaseio.com/v0/user/{}.json?print=pretty'.format(author_name)
    response = requests.get(url)
    results: dict = response.json()
    fo_path = os.path.join(data_dir,'{}.json'.format(author_name))
    print('ingesting ' + fo_path + '\n from ' + url)
    with open(fo_path, 'w') as fo:
        json.dump(results, fo, indent=1) # save a copy of json result to help with debug

def main():
    authors_story = defaultdict(list)
    authors_comment = defaultdict(list)
    data_dir = os.path.normpath(os.path.join(os.getcwd(), '..','..','data','raw'))
    stories = ingest_stories(data_dir, 'stories', 'https://hn.algolia.com/api/v1/search?query=minecraft')
    print(str(len(stories['hits'])) + ' stories.')
    for story in stories['hits']:
        cur_dir = data_dir
        print('story ' + story['objectID'] + ' by ' + story['author'])
        authors_story[story['author']].append(story['objectID'])
        _ = ingest_node(authors_comment, cur_dir, story['objectID'])

    ## TODO: ingest authors into database
    with open(os.path.join(data_dir, 'authors_story.json'), 'w') as fo:
        json.dump(authors_story, fo, indent=1)
    with open(os.path.join(data_dir, 'authors_comment.json'), 'w') as fo:
        json.dump(authors_comment, fo, indent=1)
    authors = {**authors_story, **authors_comment} # merge dicts
    authors_dir = os.path.join(data_dir, "authors")
    os.makedirs(authors_dir, exist_ok=True)
    for k, _ in authors.items():
        ingest_author(authors_dir, k)

if __name__ == '__main__':
    main()
