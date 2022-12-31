from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)

obj_list = []
API_URL = 'https://api.npoint.io/c790b4d5cab58020d391'
blogs_data = requests.get(API_URL).json()

# Collecting all the info of blogs, converting them to objects and storing them in a list
for blog in blogs_data:
    blog_object = Post(blog_id=blog["id"], blog_title=blog["title"], blog_subtitle=blog["subtitle"],
                       blog_body=blog["body"])
    obj_list.append(blog_object)


@app.route('/')
def home():
    return render_template("index.html", all_posts=obj_list)


# After clicking the read more lik
@app.route('/blogs/<int:id>')
def show_blog(id):
    for obj in obj_list:
        if obj.id == id:
            return render_template("post.html", post_obj=obj)


if __name__ == "__main__":
    app.run(debug=True)
