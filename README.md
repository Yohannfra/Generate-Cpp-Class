# Generate Cpp Class
A python script to generate cpp file content from header file

# Installation
```
sudo ./install.sh
```

# Usage:
```
Usage: gen_cpp_class hpp_file [cpp_file]
```

# Example

Your .hpp file:
```cpp
#ifndef CURSOR_H
#define CURSOR_H

#include <SFML/Graphics.hpp>

class Cursor
{
    private:
        sf::Sprite sprite;
        sf::Texture texture;
        int x;
        int y;

    public:
        Cursor();
        ~Cursor();
        void display(sf::RenderWindow& window);
        sf::Vector2i getPosition();
        void move(int direction, sf::Vector2i size, sf::View& view, sf::RenderWindow& window);
};

#endif
```

The command you need to generate the cpp file:
```
gen_cpp_class YourFile.hpp
```

It's output:
```cpp
#include "Cursor.hpp"

Cursor::Cursor()
{

}

Cursor::~Cursor()
{

}

void Cursor::display(sf::RenderWindow& window)
{

}

sf::Vector2i Cursor::getPosition()
{

}

void Cursor::move(int direction, sf::Vector2i size, sf::View& view, sf::RenderWindow& window)
{

}
```

If you want to create the cpp file just use a shell redirection

```
gen_cpp_class YourFile.hpp > YourFile.cpp
```

Now if you add a function to the header file and want to generate the cpp code
for only this function, you can then update the existing cpp file.

This will generate the cpp function and only print those that doesn't already exist
in the cpp file
```
gen_cpp_class YourFile.hpp YourFile.cpp
```

If you want to apply it to you file just use a shell redirection
```
gen_cpp_class YourFile.hpp >> YourFile.cpp
```

# How I use it

I dont use this tool from the command line like I show above.
I use it from within vim directly.

First I add this to my .vimrc
```vim
" Gen Cpp Class
command! -nargs=1 -complete=file Gclass :r !gen_cpp_class <f-args>
" Update Cpp Class
command! -nargs=1 -complete=file Uclass :r !gen_cpp_class <f-args> '%:p'
```

And to use it
```vim
:Glass path/to/file.hpp
" OR
: Uclass path/to/file.hpp
```

It will automatically write it in you buffer

# Licence
