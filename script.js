let username;
let password;
let posts = [];

const writePosts = () => {
    const messagesDiv = document.getElementById('messages');
    messagesDiv.innerHTML = '';

    posts.forEach(post => {
        const message = post.message
            .replace(/%20/g, ' ')
            .replace(/%3C/g, '<')
            .replace(/%3E/g, '>')
            .replace(/%22/g, '"')
            .replace(/{EQSIGN}/g, '=')
            .replace(/%27/g, "'");

        const commentNode = document.createElement('p');
        commentNode.innerHTML = message;
        messagesDiv.append(commentNode);
    });
};

const getPosts = () => {
  if(!username) return
    fetch('/posts.json')
        .then(data => {
            return data.json();
        })
        .then(json => {
            if(json.length > posts.length) {
              posts = json
              writePosts()
            };
        });
};

function submit() {
    if(!username) return
    let url = '/submit?';
    param =
      document.getElementById('message').value
      .replace(/=/g, '{EQSIGN}')
      .replace(/\n/g, '');
    param = username + ": " + param
    url += 'message=' + param;
    document.getElementById('message').value = ''

    fetch(url)
        .then()
        .then(() => getPosts());
}

function login() {
    username = document.getElementById('username').value;
    password = document.getElementById('password').value;

    document.getElementById('hello').innerHTML = 'Hello, ' + username + '!';
    getPosts();
}

setInterval(() => {
  if(username) getPosts()
}, 2000);