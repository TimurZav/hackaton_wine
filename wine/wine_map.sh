#!/bin/bash

PATH_ROOT="${PATH_ROOT}/wine_map"
done_path="${PATH_ROOT}"/done
if [ ! -d "$done_path" ]; then
  mkdir "${done_path}"
fi

json_path="${PATH_ROOT}"/json
if [ ! -d "$json_path" ]; then
  mkdir "${json_path}"
fi

find "${PATH_ROOT}" -maxdepth 1 -type f \( -name "*.xls*" -or -name "*.XLS*" \) ! -newermt '3 seconds ago' -print0 | while read -d $'\0' file
do

  if [[ "${file}" == *"error_"* ]];
  then
    continue
  fi

	# Will convert xlsx to json
	python3 ${PATH_SCRIPTS_DOCKER}/wine.py "${file}" "${json_path}"

  if [ $? -eq 0 ]
	then
	  mv "${file}" "${done_path}"
	else
	  mv "${file}" "${PATH_ROOT}/error_$(basename "${file}")"
	fi

done