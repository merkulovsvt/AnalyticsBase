## <u>Git</u>

---

* **Git** - место хранения истории разработки.


* **GitHub**, **GitLab** - удалённые **Git-сервера**.


* **hunk** - название разнящихся строк.


* Хороший [**тренажер**](https://learngitbranching.js.org/?locale=ru_RU).

---

### <u>[Основные команды в терминале](https://white55.ru/cmd-sh.html)</u>:

* `mkdir dir_name`  - создание новой директории.


* `cd dir_name` - переход в каталог.


* `echo "text" > file.txt` - создание файла с текстом.


* `ls` - список файлов в папке.


* `cat file.txt` - чтение файла.


* `wsl {nano|vim} file.txt` - редактирование файла. [WSL](https://learn.microsoft.com/ru-ru/windows/wsl/install),
  [VIM](https://beget.com/ru/kb/how-to/other/osnovy-raboty-s-redaktorom-vim).


* `rm file.txt` - удаление фала.


* `rm -d dir_name` - удаление пустой директории.


* `rm -d dir_name` - удаление непустой директории.

Команды с `-` являются сокращениями команд с `--`. Например `-h` == `--help`.

---

### <u>Установка Git на Windows</u>:

* Работаем с **Git** через **PowerShell**.


* Скачиваем **Git** с [официального сайта](https://git-scm.com/download).


* `git --version` - выведет версию установленного **Git**.

<u>**Установка posh-git**</u>:

1. `Install-Module posh-git -Scope CurrentUser -AllowPrerelease -Force` - установка модуля.


2. `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted` - меняем права.


3. `Import-Module posh-git` - импорт модуля.


4. `Add-PoshGitToProfile -AllHosts` - команда для автоматического импорта при запуске.

---

### <u>Конфигурация Git</u>:

* Желательно задавать `user.name` и `user.email` такими же, как и в **GitHub**, **GitLab**, ...


1. `git config --global user.name "Your name"` - задаём переменную имени.


2. `git config --global user.email your-email@mail.com` - задаём переменную почты.


3. `git config --list` - выведет весь конфиг.

<u>**Виды флагов конфигурации**</u>:

* `--local` - локально для проекта.


* `--global` - для одного пользователя на все проекты.


* `--system` - на всю операционную систему (для всех пользователей и проекты).

---

### <u>Основы Git</u>:

**Working Directory** `->` **Staging area** (**Index**) `->` **Repository**

* **Working Directory** - наша локальная директория.


* **Staging area** (**Index**) - файл, куда попадают и сохраняются изменения, которые надо включить в **commit**  
  (отправку в**Repository**).


* **Repository** - виртуальное хранилище со всеми версиями проекта.

<u>**Основные команды**</u>:

1. Переходим в нашу локальную директорию.


2. `git init` - инициализируем **Git**.


3. `git status` - отображает состояние рабочего каталога и **Index**.


4. `git add {file_name|dir_name|.} [-p]` - отправка данных из **Working Directory** в **Index**.
    * Флаг `-p` позволяет увидеть изменения, которые мы внесли и поработать с ними.


5. `git restore --staged file_name` - отменяет последние изменения файла (убирает их из **Index**).


6. `git commit [-m "Your message"]` - отправка данных из **Index** в **Repository**.


7. `git rm {file_name|dir_name}` - локальное удаление и последующий `git add`.


8. `git mv old_{file_name|dir_name} new_{file_name|dir_name}` - переименовывание файла или директории.

<u>**[Игнорирование файлов](https://phpstack.ru/php/fajl-gitignore-podrobnaa-spargalka.html#close)**</u>:

* `.gitignore` - файл формата **txt**, который можно создать и добавить в него названия (пути) файлов/директорий, на
  которые **Git** не будет обращать внимания.

Зададим его <u>**глобально**</u>:

1. `wsl nano ~/.gitignore` - создаём файл в домашнем каталоге пользователя.


2. `git config --global core.excludesfile ~/.gitignore` - меняем в конфиге путь к файлу `.gitignore`.


* `~` - домашний каталог пользователя.

Зададим его снова [<u>**локально**</u>](
https://stackoverflow.com/questions/11868447/how-can-i-remove-an-entry-in-global-configuration-with-git-config):

1. `git config --global --unset core.excludesfile` - сбрасываем настройку в конфиге.


2. `wsl nano .gitignore` - снова создаём `.gitignore` в нашей исходной директории.

### <u>Ветвление в Git</u>:

Есть два основных типа ветвлений:

1. **Тематические** (ветки - фичи)


2. **Релизные** (ветки - версии)

<u>**Основные команды**</u>:

* `HEAD` (`@`) - указатель на наше местонахождение. Информация хранится в `.git/HEAD`.


1. `git branch branch_name` - создание новой ветки `branch_name` в месте нахождения `HEAD`.


2. `git branch [-v]` - выведет список всех веток. `*` указывает на ту, где сейчас `HEAD`.
    * Флаг `-v` покажет номер последнего **commit** каждой ветки.


3. `git checkout branch_name` - переход `HEAD` на последний **commit** ветки `branch_name`.


4. `git checkout commit_hash` - переход `HEAD` на конкретный **commit**.


5. `git branch -d branch_name` - "удаление" ветки `branch_name`, те присоединение её к первоначальной.

<u>**Восстановление предыдущих версий**</u>:

* `git checkout branch_name file_name` - перенос `file_name` версии последнего **commit** из `branch_name` туда, где мы
  стоим (изменение автоматически будет в `Index`).

<u>**Переключение между ветками при незакомиченных изменениях**</u>:

1. `git stash` - локально сохраняем изменения (кешируем).


2. `git checkout other_branch` - переходим на другую ветку (в изначальной всё вернулось к последнему **commit**).


3. `git checkout my_branch` - снова возвращаемся на изначальную.


4. `git stash {apply|pop}` - загружаем локальные изменения. `apply` - не удаляет сохранение, а `pop` - удаляет.

<u>**Просмотр истории изменений**</u>:

* `git log [--oneline]` - выведет информацию по всем **commit** на всех ветках. `q` - чтобы выйти.
    * Флаг `--oneline` выведет всё в минималистичной форме.


* `git log [--oneline] branch_name` - выведет информацию по всем **commit** на ветке `branch_name`. `q` - чтобы выйти.


* `git show branch_name[~~...][:file_name\dir_name]` - посмотреть изменения в последнем **commit** ветки `branch_name`.
    * `~` - шаг назад от последнего **commit**.
    * `:file_name` - просмотр изменений только по `file_name`.


* `git show HEAD[~~...][:file_name\dir_name]` - посмотреть изменения в **commit** на месте `HEAD`.


* `git show commit_hash[~~...][:file_name\dir_name]` - посмотреть изменения конкретного **commit**.

<u>**Слияние веток методом Fast-Forward**</u>:

1. `git checkout branch_name` - переходим на ветку, отличную от изначальной.


2. `git merge zaza_branch_name` - сливаемся с `zaza_branch_name` (последний **commit** `branch_name` такой же, как и
   у `zaza_branch_name`).

<u>**Истинное слияние веток**</u>:

Берёт 3 состояния: последние коммиты каждой из веток и коммит, на котором они разделились и соединяет их.

* `git merge-base branch1_name branch2_name` - выведет хеш коммита, на котором разделились ветки.

Есть возможность того, что в коммитах файл имеет разные данные на одних позициях. Надо вручную выбирать, что оставить.

* `git config --global merge.conflictstyle diff3` - глобальная настройка хорошего вывода различий для корректировки.

1. `git merge zaza_branch_name`


2. `git checkout --{ours|theirs|merge} file_name` - выведет версии соответствующих 3 коммитов.
    * `ours` - первая ветка.
    * `theirs` - вторая ветка.
    * `merge` - возврат на состояние **merge**.


3. Делаем изменения в файле -> `git add file_name` -> `git commit`.

* `git reset --hard` - возврат на последнее состояние ветки, где **HEAD**.

### <u>Отмена изменений</u>:

Есть два основных типа **hard-reset** и **soft-reset**.

<u>**Hard-reset**</u>:

* `git reset --hard {hash_commit|HEAD~~...}` - переходит на прошлый **commit** и "удаляет" всё на своём пути.

* `git reset --hard ORIG_HEAD` - переходит на изначальный **commit**, с которого мы ушли.

<u>**SOFT-reset**</u>:
#TODO

### <u>GitHub</u>:

* **GitHub**, **GitLab** - удалённые **Git-сервера**.


* `git clone url_to_rep` - скачать проект из репозитория.
