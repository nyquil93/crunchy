��    m      �  �   �      @	  &   A	  �  h	  �   .  v  �  �   I  $  �  o            �     �     �     �     	  -        E  %   `     �     �     �  	   �     �  !   �     	          ,  1   @  +   r     �  f   �  8     H   O  +   �     �  >   �          #     6     >     Z     u  5   |  0   �     �             '   ?     g  $   �     �     �  2   �  #        A  f   R     �  >   �  
     2     +   F     r     �     �     �     �     �  8   �            .  )   O  +   y      �  -   �      �  4        J     a     z  )   �     �  l   �     G     d     }     �  "   �  S   �     *     6     <  C   P     �  .   �  $   �        $   #  $   H     m     |     �  0   �     �     �  %        2     C  6   U     �  3   �  W  �  (   /  �  X  �    !  �  �!  �   m#  S  &$  �  z%     '  %   0'  $   V'  $   {'  !   �'     �'  3   �'  "   (     )(      H(     i(     �(     �(     �(      �(     �(  !   �(     �(  7   )  ,   M)     z)  ~   �)  ?   *  l   W*  *   �*     �*  =   +     B+     V+  	   n+  "   x+  +   �+     �+  R   �+  .    ,  %   O,     u,     �,  (   �,     �,  %   �,     $-      D-  3   e-  $   �-     �-  v   �-     O.  B   ^.     �.  6   �.  2   �.  "   /     >/     \/  "   u/  
   �/     �/  c   �/      0      >0  1   _0  +   �0      �0  5   �0  '   1  A   <1     ~1     �1     �1  +   �1      2  P   2     g2     �2     �2  (   �2  '   �2  d   3     l3     }3     �3  X   �3     �3  C   4  &   W4  *   ~4  3   �4  1   �4     5  .   $5  .   S5  >   �5  %   �5  )   �5  9   6     K6  %   `6  ;   �6  '   �6  2   �6     %   X                   3   =           U          M   ;       9       l                 H   4      >          1       -       [      $   5              S      R   D   i   !   a       6   \   ,       E           k   &       .          +   `   A   "   	      b       Y       0   ?   (               Q       G   :            j   N             W       K   T   @   g      )         h       I          B       c   8   C   d         <         J   2   m   *              #   e   Z           ^           ]   7      '   
   O   F   V      _   P   L                 f   /    
  The current value for my_style is:  
'normal' will attempt to display the sites the same ways as 'trusted' does
except that it will remove any styling deemed suspicious (see the docs for
details) and will validate any image source before allowing the image to
be displayed.  If the site contains many images, this validation process
will slow down the display.  Images that can not be validated will not be
shown.  Each image is validated only once during a given Crunchy session.
         
'strict' will remove all styling and image on the page.  It will result
in the fastest display, but one that will likely be the least visually
appealing.
         
'trusted' should only be used for sites that you are convinced will
not attempt to insert malicious code.  Sites that allow users to post
comments, or worse, that allow users to edit (such as wikis) should not
be set to 'trusted'. With 'trusted' selected, Crunchy will display the
site as closely as it can to the wayt the original looked using only
 your browser.
         
Crunchy will remove any pre-existing javascript code on the page as
well as a number of html elements that could be used to hide some
javascript code.
         
Selection of a 'display MODE' will result in the same processing by Crunchy
as the selection of 'MODE' except that no interactive elements
(such as a Python interpreter)
will be inserted in the page, thereby preserving the normal browser
sandbox to protect your computer from malicious code. 
You can change some of the default values by Crunchy, just like
you can obtain this help message, using either an interpreter
prompt or an editor, and assigning the desired value to a given
variable.  Some of these variables are "fixed", which means that
their value can not be changed by the user.
-
Here are the values of some variables currently used by Crunchy.
   The current value is:   %d elements were removed. -   Crunchy security level:   No elements were removed.   One element was removed. -   View report   by the user's choice specified in %s.styles
 # no code entered by user
 (Fixed) Temporary working directory:  (Fixed) User home directory:  An exception was raised: Approve Attribute Attribute (if relevant) Before browsing any further ...

 Cancel Confirm the security levels Confirmation code:  Congratulations, your code passed all (%d) tests! Congratulations, your code passed the test! Copy code sample Crunchy could not open the page you requested. This could be for one of anumber of reasons, including: Crunchy will attempt to provide friendly error messages. Crunchy's error messages will be similar to Python's default tracebacks. Crunchy: could not style the following code Directory Listing Do you wish to retain the existing settings for these sites?

 Error on line Error on line %s:
 Execute Execute as external program Execute as separate thread Host:  If set to True, Crunchy's default styles are replaced If you want to preserve the existing selection,  Illegal path, page not found. Invalid choice for %s.dir_help Invalid choice for %s.doc_help Invalid choice for %s.editarea_language Invalid choice for %s.language Invalid choice for %s.local_security Invalid choice for %s.my_style Invalid choice for %s.no_markup Invalid choice for %s.override_default_interpreter Invalid choice for %s.site_security Load Python file Note: while this is a valid choice, this choice is not available for a language provided by editarea.  Number of times Parsing error occurred in the following Python code.
Info: %s. Remove all Removed: attribute, or attribute value not allowed Removed: style tag or attribute not allowed Removed: tag not allowed Save Python file Save and Run Select site security level Tag Tag removed The choices for "pre" tag without Crunchy markup are %s
 The choices for dir_help are %s
 The choices for doc_help are %s
 The choices for editarea_language are %s
 The choices for friendly tracebacks are %s
 The choices for language are %s
 The choices for local_security levels are %s
 The choices for my_style are %s
 The choices for override_default_interpreter are %s
 The current value is:  The expected result was: The following example failed: The language choice for editarea remains  The page doesn't exist. The path you requested was illegal, examples of illegal paths include those containing the .. path modifier. The path you requested was:  The result obtained was: The valid choices are:  There was no test to satisfy. Type %s.help for more information. Use 'Save and Run' to execute programs (like pygame and GUI based ones) externally. User's code Value Value (if relevant) You can change any of them before clicking on the approve button.

 You code failed the test. You may select a site specific security level: Your code failed %s out of %s tests. Your code failed all (%d) tests. Your program tried to exit Crunchy.
 builtins not defined in console yet. called by line editarea_language also set to:  editarea_language set to:  friendly attribute must be set to True or False. language set to:  my_style set to:  override_default_interpreter set to:  remove from list security set to:  simply dismiss this window by clicking on the X above. site security set to:  with "image_file   file_name" as a required option. Project-Id-Version: Crunchy
POT-Creation-Date: 
PO-Revision-Date: 2007-08-23 22:13-0400
Last-Translator: André Roberge <andre.roberge@gmail.com>
Language-Team: André Roberge <andre.roberge@gmail.com>
MIME-Version: 1.0
Content-Type: text/plain; charset=utf-8
Content-Transfer-Encoding: 8bit
X-Poedit-Language: French
X-Poedit-Country: CANADA
 
  La valeur assignée à my_style est : 
'normal' fera en sorte que Crunchy traitera le site presque comme pour 'trusted'
sauf qu'il éliminera tout style apparaissant suspect (voir la documentation)
et validera tout fichier image avant de permettre son inclusion dans la page.
Si la page contient plusieurs images, le processus de validation prendra
un certain temps.  Chaque image n'est validée qu'une seule fois durant
une même session avec Crunchy.
         
'strict' fera en sorte que tous les styles et images seront éliminés.
C'est le choix le plus rapide, mais d'apparence visuelle le moins intéressant.
         
'trusted' devrait être seulement utilisé lorsque vous êtes convaincu que le site
est conçu sans possibilité de code malicieux.  Les sites qui permettent aux utilisateurs
d'ajouter des commentaires, ou pire, d'éditer le site (tels que les wikis) ne devraient pas
se mériter le choix de 'trusted'. Avec le choix 'trusted', Crunchy reproduit 
le site aussi fidèlement qu'il le peut, si on compare avec ce que votre
fureteur donne sans Crunchy.
         
Crunchy enlevera tout code javascript inséré auparavant dans la page
ainsi qu'un nombre de balises html qui pourraient être utilisées pour
camoufler des codes javascript.
         
La sélecton de 'display MODE' aura comme résultat le même traitement par Crunchy
que la sélection de 'MODE' sauf qu'aucun élément interactif
(tel qu'un interprète Python)
ne sera inséré dans la page, préservant ainsi les barrières de sécurité
normale de votre fureteur protégeant votre ordinateur contre des codes malicieux. 
Vous pouvez changez certaines des choix par défaut de Crunchy, tout comme
vous pouvez voir ce message, en utilisant une invite de commande 
ou un éditeur, et assigner la valeur désirée à une certaine variable.
Certaines de ces variables sont " fixées", ce qui veut dire que
leur valeur ne peut pas être changée par l'utilisateur.
-
Voici les valeurs des variables présentement utilisées par Crunchy.
  La valeur actuelle est : %d éléments ont été éliminés. - Le niveau de sécurité de Crunchy:  Aucun élément n'a été éliminé. Un élément a été éliminé. - Voir le rapport par le choix de l'usager spécifié dans %s.styles
 # pas de code entré par l'usager
 (Fixé) répertoire temporaire (Fixé) répertoire de l'usager: Une exception est survenue : Approbation Attribut Attribut (si pertinent) Avant de fureter davantage ...

 Annuler Confirmer le niveau de sécurité Code de confirmation : Félicitation, votre code a passé tous les (%d) tests! Félicitations, votre code a passé le test! Copier l'échantillon de code Crunchy n'a pu ouvrir la page demandée.  Plusieurs causes différentes peuvent être à l'origine de cette erreur, incluant : Crunchy tentera de donner des messages d'erreurs plus cordiaux. Les messages d'erreurs de Crunchy seront semblables aux messages d'erreurs standard (tracebacks)  de Python. Crunchy ne peut pas styler le code suivant Liste du répertoire Désirez-vous conserver les choix existants pour ces sites?

 Erreur à la ligne  Erreur à la ligne %s:
 Exécuter Exécuter comme programme externe. Exéctuer comme processus (thread) distinct Hote: Si la valeur assignée est True, les styles par défaut de Crunchy sont remplacés Si vous désirez préserver le choix existant, Parcours illégal, page non trouvée. Choix invalide pour %s.dir_help Choix invalide pour %s.doc_help Choix invalide pour %s.editarea_language Choix invalide pour %s.language Choix invalide pour %s.local_security Choix invalide pour %s.my_style Choix invalide pour %s.no_markup Choix invalide pour %s.override_default_interpreter Choix invalide pour %s.site_security Charger le fichier Python Notez que, bien que ceci soit un choix valide, ce choix n'est pas disponible parmi les langues définies pour editarea Nombre de fois Erreur de compréhension du code Python suivant.
Information : %s. Éliminez tout. Éliminé: attibut ou valeur de l'attribut non permis. Éliminé: étiquette style ou attribut non permis Éliminé: étiquette non permise. Sauvegarder le fichier Python Sauvegarder et exécuter Choisissez le niveau de sécurité Étiquette Étiquette éliminée Les choix pour l'étiquette "pre" utilisée par Crunchy en l'absence de balisage (markup) sont  %s
 Les choix pour dir_help sont %s
 Les choix pour doc_help sont %s
 Les choix valides pour editarea_language sont %s
 Les choix pour l'attribut friendly sont %s
 Les choix pour language sont %s
 Les choix valides pour local_security levels sont %s
 Les chix valides pour my_style sont %s
 Les choix pour la  variable override_default_interpreter sont %s
 La valeur actuelle est : Le résultat attendu était : L'exemple suivant a échoué : Le choix de la langue pour editarea demeure La page n'existe pas. Le parcours que vous avez demandé est illégal, possiblement en raison de ceci: Le parcours requis était : Le résultat obtenu est : Les choix valides sont : Il n'y avait pas de tests à satisfaire. Entrez %s.help pour plus d'information. Utiliser 'Sauvegarder et exécuter' pour exécuter des programmes (comme les GUI) de façon externe. Code de l'usager Valeur Valeur (si pertinente) Vous pouvez changer ceux que vous voulez avant de cliquer sur le bouton d'approbation.

 Votre code a échoué le test. Vous pouvez choisir un niveau de sécurité spécifique à ce site. Votre code a échoué %s des %s tests. Votre code a échoué tous les (%d) tests. Votre programme a tenté de faire avorter Crunchy.
 Les "builtins" ne sont pas définis en ce moment. appelé à la ligne  la valeur assignée à editarea_language est : la valeur assignée à editarea_language est : Le choix de l'attribut friendly soit être soit True ou False. la valeur assignée à language est : la valeur assignée à my_style set est : La valeur assignée à override_default_interpreter est : Retirer de la liste. la valeur assignée à security est : veuillez fermer la fenêtre en cliquant sur le X ci-dessus. niveau de sécurité pour ce site est : avec "nom du fichier image" comme argument requis. 