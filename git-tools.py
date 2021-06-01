1，在本地创建SSH key
ssh-keygen -t rsa -C "your_email@youremail.com"
2，回到github，进入Account Settings，左边选择SSH Keys，Add SSH Key,title随便填，粘贴key
3，接下来我们要做的就是把本地仓库传到github上去，在此之前还需要设置username和email，因为github每次commit都会记录他们
git config --global user.name "your name"  
git config --global user.email "your_email@youremail.com"
4，为了验证是否成功，在Git bash下输入：ssh -T git@github.com 
5，git clone git@github.com:yourName/yourRepo.git  
6, git add  <file>
7, git commit -m 'first'
8, git status
9, git push origin master
