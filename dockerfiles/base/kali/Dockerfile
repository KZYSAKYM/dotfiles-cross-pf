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
    && echo "en_US UTF-8" > /etc/locale.gen    \
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

# For SSH
RUN mkdir /var/run/sshd
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd
RUN echo '[ "$(ps aux | grep sshd)" ] || nohup /usr/sbin/sshd -D &' >> /etc/profile
# For sudo bug fix
RUN echo "Set disable_coredump false" > /etc/sudo.conf

# For Shared Volume
RUN mkdir /home/develop/work
VOLUME /home/develop/work

RUN chown -R develop:develop /home/develop

ENTRYPOINT /usr/sbin/sshd -D
