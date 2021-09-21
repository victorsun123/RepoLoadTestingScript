import argparse
import os 
from random import choice
import shutil 
from string import ascii_lowercase


parser = argparse.ArgumentParser(description='Repo Dimensions')
parser.add_argument('--num_files', type=int, nargs='?',
                    default=50, help='Number of files in repo')
parser.add_argument('--num_notebooks', type=int, nargs='?',
                    default=50, help='Number of files in repo')
parser.add_argument('--file_size', type=int, nargs='?',
                    default=20, help='file size in kb')
parser.add_argument('--folder_name', type=str, nargs='?',
 					default='folder', help='file size in kb')

kb_size = 1024
lis=list(ascii_lowercase)

args = parser.parse_args()


def generate_file(num_files, num_notebooks, file_size, folder_name):
	if os.path.isdir(folder_name):
		shutil.rmtree(folder_name)
	os.mkdir(folder_name)

	for i in range(num_files):
		with open("%s/file_%s.txt" % (folder_name, i), "w") as file:
			# file.write(os.urandom(file_size*kb_size))
			file.write(''.join(choice(lis) for _ in xrange(file_size*kb_size)))
	for i in range(num_notebooks):
		with open("%s/file_%s.py" % (folder_name, i), "w+") as file:
			file.write("# Databricks notebook source\n")
			file.write(''.join(choice(lis) for _ in xrange(file_size*kb_size)))

	os.chdir(folder_name)
	os.system('git init')
	os.system ('git remote add origin git@github.com:victorsun123/benchmark_repo.git')
	os.system('git add -A')
	os.system('git commit -m "commit"')
	os.system('git push origin master --force')

generate_file(args.num_files, args.num_notebooks, args.file_size, args.folder_name)
