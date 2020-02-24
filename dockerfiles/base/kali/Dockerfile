FROM kalilinux/kali

MAINTAINER KZYSAKYM

EXPOSE 20 21 22 80 8080 8888

RUN DEBIAN_FRONTEND=noninteractive apt-get update &&  \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
    sudo        \
    apt-utils   \
    coreutils   \
    git         \
    python3     \
    python3-pip \
    locales     \
    && pip3 install pyyaml  \
    && echo "en_US.UTF-8" > /etc/locale.gen    \
    && locale-gen

RUN adduser develop \
        --home /home/develop	\
        --disabled-login --gecos ''
ENV HOME /home/develop
WORKDIR /home/develop

RUN git clone https://github.com/KZYSAKYM/dotfiles-cross-pf \
        /home/develop/dotfiles-cross-pf &&                  \
    cd  /home/develop/dotfiles-cross-pf &&                  \
    python3 main.py

RUN git clone https://github.com/Shougo/dein.vim            \
        /home/develop/.cache/dein/repos/github.com/Shougo/dein.vim

RUN echo "zsh" >> /home/develop/.bashrc
RUN echo "export LANGUAGE=C.UTF-8" >> /home/develop/.zshenv
RUN echo "export LANG=C.UTF-8" >> /home/develop/.zshenv
RUN echo "export LC_ALL=C.UTF-8" >> /home/develop/.zshenv

RUN git clone https://github.com/powerline/fonts.git --depth=1 /tmp/fonts
WORKDIR /tmp/fonts
RUN ./install.sh

# Set tentative passwd. Please reset with your own password.
RUN printf "password\npassword\n" | passwd develop
RUN usermod -aG sudo develop

RUN chown -R develop:develop /home/develop

ENTRYPOINT /bin/su - develop
