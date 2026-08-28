# Table of contents 
### (I just love this feature when I see it in other repos)
- [aptlist](#aptlist)
- [why I made aptlist](#why-I-made-aptlist)
- [The name](#The-name)
- [Installation](#Installation)
- [Usage](#Usage)
- [Conclusion](#Conclusion)

# aptlist
an attempt by a bad programmer to create an APT-based package browser. inspired by cargo-seek https://crates.io/crates/cargo-seek

# why I made aptlist
aptlist is just a for-fun repo that i made as my first real public repo/project, and the more I think about it the more useless it feels.
am not a bad programmer am just a new programmer and this is just me messing around trying to make something simple and useful

# The name 
I kinda just looked at lsusb and how simple it is so am trying to implement this simplicity while still making it look modern and easy to navigate around and thats how I came up with **_aptlist_** and you can run it using `aptls`

# Installation
just run this sequence of commands and you should be good
```bash
#This will clone the repo, make the script executable, and symlink it into ~/.local/bin 
git clone https://github.com/KigoryGH/aptlist.git
cd aptlist
chmod +x aptls
mkdir -p ~/.local/bin
ln -sf "$(pwd)/aptls" ~/.local/bin/aptls
cd
```
# Usage
am gonna be honest with you aptlist turned out to be one of those programs that are used once for fun and
then thrown away, so as the guy who made this program I only found one use case and it is if you want to see what random commands do you can go to them and check them out using apt ls it's like running apt show <package>
but you dont know the package name, overall am proud that this is my first real repo.
## preview
<img src="preview.gif" width="700">

# Conclusion
this was a repo made for fun by me as a first repo and even though the project came out 99% useless and heavy and 20% of the code is claude  I still was proud of myself as this is my first repo and I enjoyed
the experience and learned a lot about textual and git. i'd recommend that other people that want to create a repo to not overthink it and  go for it even if it's useless.
I think I can do better if I knew how to code in python I literally made this by looking at syntax from other repos and trial and error for hours.
Thanks for just clicking on this repo :)
