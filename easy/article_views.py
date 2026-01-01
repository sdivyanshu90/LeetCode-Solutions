import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    same_author_viewer = views[views['author_id'] == views['viewer_id']]
    result = same_author_viewer[['author_id']].drop_duplicates().sort_values(by='author_id')
    result.rename(columns={'author_id': 'id'}, inplace=True)
    return result

def test_article_views():
    data = {
        'author_id': [1, 2, 3, 1, 2, 3, 4],
        'viewer_id': [1, 2, 4, 3, 2, 3, 4]
    }
    views = pd.DataFrame(data)
    result = article_views(views)
    print(result)
    # Expected output:
    #    id
    # 0   1
    # 1   2
    # 5   3
    # 6   4

test_article_views()