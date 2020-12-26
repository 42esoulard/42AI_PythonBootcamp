#!/usr/bin/env python
# -*- coding: utf-8 -*-

languages = {
'Python': 'Guido van Rossum', 
'Ruby': 'Yukihiro Matsumoto', 
'PHP': 'Rasmus Lerdorf',
}

for key, value in languages.items():
	print(key, "was created by", value)
