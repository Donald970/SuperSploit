#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <dirent.h>
#include <unistd.h>

char** read_exploit_data(int* count) {
    char install_location[256];
    char data_install_location[256];
    char database[256];
    snprintf(install_location, sizeof(install_location), "/home/%s/supersploit", getlogin());
    snprintf(data_install_location, sizeof(data_install_location), "/home/%s/supersploit/.data", getlogin());
    snprintf(database, sizeof(database), "%s/.data", install_location);

    DIR *dir;
    struct dirent *entry;
    char exploit_path[512];
    char file_path[512];
    char **data = NULL;
    *count = 0;

    snprintf(exploit_path, sizeof(exploit_path), "%s/exploits", install_location);
    dir = opendir(exploit_path);
    if (dir == NULL) {
        perror("opendir");
        return NULL;
    }

    while ((entry = readdir(dir)) != NULL) {
        if (entry->d_type == DT_DIR && strcmp(entry->d_name, ".") != 0 && strcmp(entry->d_name, "..") != 0) {
            char sub_exploit_path[512];
            snprintf(sub_exploit_path, sizeof(sub_exploit_path), "%s/%s", exploit_path, entry->d_name);
            DIR *sub_dir = opendir(sub_exploit_path);
            struct dirent *sub_entry;

            while ((sub_entry = readdir(sub_dir)) != NULL) {
                if (sub_entry->d_type == DT_REG) {
                    snprintf(file_path, sizeof(file_path), "%s/%s", sub_exploit_path, sub_entry->d_name);
                    FILE *rfile = fopen(file_path, "r");
                    if (rfile) {
                        char *buffer = NULL;
                        size_t size = 0;
                        ssize_t read;

                        while ((read = getline(&buffer, &size, rfile)) != -1) {
                            if (strstr(buffer, "# DETAILS #") != NULL) {
                                data = realloc(data, (*count + 1) * sizeof(char*));
                                data[*count] = strdup(buffer);
                                (*count)++;
                            }
                        }
                        free(buffer);
                        fclose(rfile);
                    }
                }
            }
            closedir(sub_dir);
        }
    }
    closedir(dir);
    return data;
}

