# Downloads Organizer

![GitHub repo size](https://img.shields.io/github/repo-size/jadonlai/downloads-organizer)
![GitHub contributors](https://img.shields.io/github/contributors/jadonlai/downloads-organizer)
![GitHub stars](https://img.shields.io/github/stars/jadonlai/downloads-organizer?style=social)
![GitHub forks](https://img.shields.io/github/forks/jadonlai/downloads-organizer?style=social)

Downloads organizer is a simple Python script that allows users to organize their downloads directory into different subdirectories, based on file type.

This is done by creating subdirectories labeled `downloads_<filetype>`. Each corresponding directory and file in the downloads directory is then moved to its corresponding subdirectory.

## Prerequisites

None

## Installing Downloads Organizer

To install Downloads Organizer, follow these steps:

```
git clone https://github.com/jadonlai/downloads-organizer.git
```

## Using Downloads Organizer

To use Downloads Organizer, run:

```
./main.py
```

You may need to give execute permissions to the script. To do so, run:

```
chmod +x main.py
```

You may also want to run the script in the background, to automatically organize the downloads directory. On MacOS, you can do this using crontab:

```
crontab -e
```

```
* * * * * /usr/bin/python /path/to/downloads-organizer/main.py
```

To verify the task is scheduled:

```
crontab -l
```

## Contributing to Downloads Organizer

To contribute to Downloads Organizer, follow these steps:

1. Fork this repository.
2. Create a branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`
4. Push to the original branch: `git push origin <project name>/<location>`
5. Create the pull request.

Alternatively see the GitHub documentation on [creating a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

## Contact

If you want to contact me you can reach me at <jadonlai.314@gmail.com>.

## License

This project uses the following license: [MIT License](https://github.com/jadonlai/downloads-organizer?tab=MIT-1-ov-file).
