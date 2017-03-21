# 認証する
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
from wordpress_xmlrpc.methods.users import GetUserInfo
wp = Client('http://thisissample.wp.xdomain.jp/xmlrpc.php', 'sample007', 'vvq1meoczwc7')

# 投稿する
post = WordPressPost()
# タイトル
post.title = 'My new title'
post.content = 'This is the body of my new post.'
# タグ
post.terms_names = {
'post_tag': ['test', 'firstpost'],
'category': ['Introductions', 'Tests']
}

# 投稿URL
post.slug = 'sample'

# 投稿日時

# 投稿状態　指定なしで下書き
post.post_status="publish"

# 投稿する。
wp.call(NewPost(post))

