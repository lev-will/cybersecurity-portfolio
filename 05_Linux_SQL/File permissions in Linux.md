# File permissions in Linux

## Project description

As a security professional, I mainly work with the research team. I
ensure users on the team are authorized with the appropriate
permissions. This helps keep the system secure.

My task is to examine existing permissions on the file system and
determine if the permissions match the authorization that should be
given. If they do not match, I'll need to modify the permissions to
authorize the appropriate users and remove any unauthorized access.

## Check file and directory details

After navigating to the /home/researcher2/projects directory, I used the
ls -la command to show existing permissions for all subdirectories and
files (including hidden files). There was a hidden .project_x.txt file,
a drafts subdirectory and then four additional files.

## Describe the permissions string

The 10 character string of the first column helps me identify the
permissions for each file. If the first character is a 'd' that means
this is a directory, if it's a hyphen'-'then it's a file.

Following that character, the first three represent the 'user', second
three 'group', third three 'other.' The following is the description for
each letter: r-read, w-write, x-execute; and if one of these letters is
replaced with a hyphen '-' it indicates that this permission is not
granted.

Current file permissions in projects directory are as follows:

-rw\--w\-\-\-- 1 researcher2 research_team 46 Jun 22 20:21
.project_x.txt

drwx\--x\-\-- 2 researcher2 research_team 4096 Jun 22 20:21 drafts

-rw-rw-rw- 1 researcher2 research_team 46 Jun 22 20:21 project_k.txt

-rw-r\-\-\-\-- 1 researcher2 research_team 46 Jun 22 20:21 project_m.txt

-rw-rw-r\-- 1 researcher2 research_team 46 Jun 22 20:21 project_r.txt

-rw-rw-r\-- 1 researcher2 research_team 46 Jun 22 20:21 project_t.txt

## Change file permissions

Given my instructions, \'others' should not have write access to any
files. Therefore I used the chmod o-w project_k.txt command to remove
the write access from the project_k.txt file.

## Change file permissions on a hidden file

Per instructions, I used the chmod u-w,g=r .project_x.txt command to
adjust permissions on the hidden file to allow the user and group to
read the file. I know the .project_x.txt file is a hidden file because
it starts with a period '.' The command shows how I removed the write
access from the user 'u-w' and I adjusted the access to the group to
read only 'g=r'.

## Change directory permissions

Per instructions, I used the chmod g-x drafts command to adjust access
to the drafts directory, allowing only the user researcher2 to have
access to that directory and its contents.

## Summary

I adjusted the permissions to match the level of authorization the
organization wanted for files and directories in the projects directory.
First, I used ls -la to check the permissions for the directory. This
helped me to see what adjustments I needed to make. I then used the
chmod command multiple times to change the permissions on files and
directories.
