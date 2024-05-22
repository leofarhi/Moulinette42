from BaseLib import *
from BaseMan import *

txt =\
"""
1. isalpha

int isalpha(int c);

Description : Vérifie si le caractère passé est une lettre alphabétique.

#######################################################################################################
2. isdigit

int isdigit(int c);

Description : Vérifie si le caractère passé est un chiffre (0-9).

#######################################################################################################
3. isalnum

int isalnum(int c);

Description : Vérifie si le caractère passé est une lettre alphabétique ou un chiffre.

#######################################################################################################
4. isascii

int isascii(int c);

Description : Vérifie si le caractère passé est un caractère ASCII (valeur entre 0 et 127).

#######################################################################################################
5. isprint

int isprint(int c);

Description : Vérifie si le caractère passé est imprimable, y compris l'espace.

#######################################################################################################
6. strlen

size_t strlen(const char *s);

Description : Calcule la longueur d'une chaîne de caractères, excluant le caractère nul de fin.

#######################################################################################################
7. memset

void *memset(void *s, int c, size_t n);

Description : Remplit les premiers n octets de la zone mémoire pointée par s avec l'octet c.

#######################################################################################################
8. bzero

void bzero(void *s, size_t n);

Description : Met à zéro (remplit avec des octets zéro) les n premiers octets de la zone mémoire pointée par s.

#######################################################################################################
9. memcpy

void *memcpy(void *dest, const void *src, size_t n);

Description : Copie n octets de la mémoire src vers dest. Les deux zones ne doivent pas se chevaucher.

#######################################################################################################
10. memmove

void *memmove(void *dest, const void *src, size_t n);

Description : Copie n octets de src vers dest. Les zones peuvent se chevaucher.

#######################################################################################################
11. strlcpy

size_t strlcpy(char *dst, const char *src, size_t dstsize);

Description : Copie une chaîne de caractères de src vers dst en s'assurant que la destination soit nulle terminée et ne dépasse pas dstsize - 1 caractères.

#######################################################################################################
12. strlcat

size_t strlcat(char *dst, const char *src, size_t dstsize);

Description : Concatène la chaîne src à la fin de dst en s'assurant que la destination soit nulle terminée et ne dépasse pas dstsize - 1 caractères.

#######################################################################################################
13. toupper

int toupper(int c);

Description : Convertit une lettre minuscule en majuscule.

#######################################################################################################
14. tolower

int tolower(int c);

Description : Convertit une lettre majuscule en minuscule.

#######################################################################################################
15. strchr

char *strchr(const char *s, int c);

Description : Recherche la première occurrence du caractère c dans la chaîne s.

#######################################################################################################
16. strrchr

char *strrchr(const char *s, int c);

Description : Recherche la dernière occurrence du caractère c dans la chaîne s.

#######################################################################################################
17. strncmp

int strncmp(const char *s1, const char *s2, size_t n);

Description : Compare les premiers n caractères des chaînes s1 et s2.

#######################################################################################################
18. memchr

void *memchr(const void *s, int c, size_t n);

Description : Recherche la première occurrence de l'octet c dans les n premiers octets de la zone mémoire pointée par s.

#######################################################################################################
19. memcmp

int memcmp(const void *s1, const void *s2, size_t n);

Description : Compare les n premiers octets des zones mémoire s1 et s2.

#######################################################################################################
20. strnstr

char *strnstr(const char *big, const char *little, size_t len);

Description : Recherche la première occurrence de la sous-chaîne little dans les premiers len caractères de big.

#######################################################################################################
21. atoi

int atoi(const char *nptr);

Description : Convertit la chaîne de caractères nptr en entier (int).

#######################################################################################################
22. calloc

void *calloc(size_t nmemb, size_t size);

Description : Alloue de la mémoire pour un tableau de nmemb éléments de taille size et initialise la mémoire allouée à zéro.

#######################################################################################################
23. strdup

char *strdup(const char *s);

Description : Duplique la chaîne de caractères s en allouant la mémoire nécessaire et renvoie un pointeur vers la nouvelle chaîne.

#######################################################################################################
24. ft_substr

char *ft_substr(char const *s, unsigned int start, size_t len);

Description : Alloue (avec malloc(3)) et retourne une chaîne decaractères issue de la chaîne 's'.
Cette nouvelle chaîne commence à l'index 'start' et a pour taille maximale 'len'

#######################################################################################################
25. ft_strjoin

char *ft_strjoin(char const *s1, char const *s2);

Description : Alloue (avec malloc(3)) et retourne une nouvelle chaîne, résultat de la concaténation de s1 et s2.

#######################################################################################################
26. ft_strtrim

char *ft_strtrim(char const *s1, char const *set);

Description : Alloue (avec malloc(3)) et retourne une copie de la chaîne 's1', sans les caractères spécifiés dans 'set' au début et à la fin de la chaîne de caractères.

#######################################################################################################
27. ft_split

char **ft_split(char const *s, char c);

Description : Alloue (avec malloc(3)) et retourne un tableau de chaînes de caractères obtenu en séparant 's' à l'aide du caractère 'c', utilisé comme délimiteur.
Le tableau doit être terminé par NULL

#######################################################################################################
28. ft_itoa

char *ft_itoa(int n);

Description : Alloue (avec malloc(3)) et retourne une chaîne de caractères représentant l'entier 'n' reçu en argument. Les nombres négatifs doivent être gérés.

#######################################################################################################
29. ft_strmapi

char *ft_strmapi(char const *s, char (*f)(unsigned int, char));

Description : Applique la fonction 'f' à chaque caractère de la chaîne de caractères passée en argument pour créer une nouvelle chaîne de caractères (avec malloc(3)) résultant des applications successives de 'f'.

#######################################################################################################
30. ft_striteri

void ft_striteri(char *s, void (*f)(unsigned int, char*));

Description : Applique la fonction 'f' à chaque caractère de la chaîne de caractères transmise comme argument, et en passant son index comme premier argument.
Chaque caractère est transmis par adresse à 'f' afin d'être modifié si nécessaire.

#######################################################################################################
31. ft_putchar_fd

void ft_putchar_fd(char c, int fd);

Description : Écrit le caractère 'c' sur le descripteur de fichier donné.

#######################################################################################################
32. ft_putstr_fd

void ft_putstr_fd(char *s, int fd);

Description : Écrit la chaîne de caractères 's' sur le descripteur de fichier donné.

#######################################################################################################
33. ft_putendl_fd

void ft_putendl_fd(char *s, int fd);

Description : Écrit La chaîne de caractères 's' sur le descripteur de fichier donné suivie d'un retour à la ligne.

#######################################################################################################
34. ft_putnbr_fd

void ft_putnbr_fd(int n, int fd);

Description : Écrit l'entier 'n' sur le descripteur de fichier donné.


BONUS :

#######################################################################################################
35. ft_lstnew

t_list *ft_lstnew(void *content);

Description : Alloue (avec malloc(3)) et renvoie un nouvel élément. La variable membre 'content' est initialisée à l'aide de la valeur du paramètre 'content'. La variable 'next' est initialisée à NULL.

#######################################################################################################
36. ft_lstadd_front

void ft_lstadd_front(t_list **lst, t_list *new);

Description : Ajoute l'élément 'new' au début de la liste.

#######################################################################################################
37. ft_lstsize

int ft_lstsize(t_list *lst);

Description : Compte le nombre d'éléments de la liste.

#######################################################################################################
38. ft_lstlast

t_list *ft_lstlast(t_list *lst);

Description : Renvoie le dernier élément de la liste.

#######################################################################################################
39. ft_lstadd_back

void ft_lstadd_back(t_list **lst, t_list *new);

Description : Ajoute l'élément 'new' à la fin de la liste.

#######################################################################################################
40. ft_lstdelone

void ft_lstdelone(t_list *lst, void (*del)(void *));

Description : Libère la mémoire de l'élément passé en argument en utilisant la fonction 'del' puis avec free(3). La mémoire de 'next' ne doit pas être free.

#######################################################################################################
41. ft_lstclear

void ft_lstclear(t_list **lst, void (*del)(void *));

Description : Supprime et libère la mémoire de l'élément passé en paramètre, et de tous les éléments qui suivent, à l'aide de 'del' et de free(3)
Enfin, le pointeur initial doit être mis à NULL.

#######################################################################################################
42. ft_lstiter

void ft_lstiter(t_list *lst, void (*f)(void *));

Description : Itère sur la liste 'lst' et applique la fonction 'f' au contenu chaque élément.

#######################################################################################################
43. ft_lstmap

t_list *ft_lstmap(t_list *lst, void *(*f)(void *), void (*del)(void *));

Description : Itère sur la liste 'lst' et applique la fonction 'f 'au contenu de chaque élément. Crée une nouvelle liste résultant des applications successives de 'f'. La fonction 'del' est là pour détruire le
contenu d'un élément si nécessaire.
"""

@AddMan('')
class MainMan(BaseMan):
	def Print(self):
		print(txt)