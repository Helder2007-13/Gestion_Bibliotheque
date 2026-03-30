import pymysql
import tkinter as tk
from tkinter import ttk,messagebox
def connecter_db(self):
        try:
            # Configuration de la connexion à la base de données
            bibliotheque = pymysql.connect(
                host='localhost',
                user='root', 
                password='', 
                database='gestion_bibliothèque'
            )
            
            
            print("Connexion réussie à MySQL !")
            
           
            
            return bibliotheque

        except pymysql.MySQLError as e:
            
            print(f"Erreur lors de la connexion : {e}")
            messagebox.showerror("Erreur de Connexion", f"Impossible de se connecter à la base de données :\n{e}")
            return None

class ApplicationBibliotheque:
        def __init__(self, root):
            print("Démarrage de l'application...") 
            self.root = root
            self.root.title("Système de Gestion de Bibliothèque")
            self.root.geometry("800x600")

            # Création du système d'onglets
            self.onglets = ttk.Notebook(self.root)
            self.onglets.pack(expand=1, fill="both")

            # Création des cadres (frames) pour chaque table
            self.tab_livre = ttk.Frame(self.onglets)
            self.tab_abonne = ttk.Frame(self.onglets)
            self.tab_emprunt = ttk.Frame(self.onglets)
            self.tab_admin = ttk.Frame(self.onglets)

            # Ajout des onglets au Notebook
            self.onglets.add(self.tab_livre, text="📚 Livres")
            self.onglets.add(self.tab_abonne, text="👥 Abonnés")
            self.onglets.add(self.tab_emprunt, text="🔄 Emprunts")
            self.onglets.add(self.tab_admin, text="🔐 Bibliothécaires")
            
            self.db = self.connecter_db()

            try:
                self.db = self.connecter_db()
                print("Connexion OK")
                
               
                self.construire_tab_livre()
                self.construire_tab_abonne()
                self.construire_tab_emprunt()
                self.construire_tab_admin()
                print("Interface construite !")
                
            except Exception as e:
                print(f"ERREUR CRITIQUE durant l'initialisation : {e}")
                messagebox.showerror("Erreur de lancement", f"Détail : {e}")
        def connecter_db(self):
            import pymysql
            return pymysql.connect(
                host="localhost", 
                user="root", 
                password="", 
                database="gestion_bibliothèque"
            ) 
                
        def construire_tab_livre(self):
           
            tk.Label(self.tab_livre, text="Gestion du Stock de Livres", font=("Arial", 14)).pack(pady=10)
            
                # --- ZONE DE SAISIE (Frame) ---
            frame_saisie = tk.Frame(self.tab_livre)
            frame_saisie.pack(pady=10)

            tk.Label(frame_saisie, text="Titre :").grid(row=0, column=0, padx=5, pady=5)
            self.ent_titre = tk.Entry(frame_saisie, width=30)
            self.ent_titre.grid(row=0, column=1, padx=5, pady=5)

            tk.Label(frame_saisie, text="Auteur :").grid(row=1, column=0, padx=5, pady=5)
            self.ent_auteur = tk.Entry(frame_saisie, width=30)
            self.ent_auteur.grid(row=1, column=1, padx=5, pady=5)

            tk.Label(frame_saisie, text="Genre :").grid(row=2, column=0, padx=5, pady=5)
            self.ent_genre = tk.Entry(frame_saisie, width=30)
            self.ent_genre.grid(row=2, column=1, padx=5, pady=5)

            tk.Label(frame_saisie, text="Année de Pub :").grid(row=3, column=0, padx=5, pady=5)
            self.ent_annee = tk.Entry(frame_saisie, width=30)
            self.ent_annee.grid(row=3, column=1, padx=5, pady=5)

            tk.Label(frame_saisie, text="Disponible (1=Oui / 0=Non) :").grid(row=4, column=0, padx=5, pady=5)
            self.ent_dispo = tk.Entry(frame_saisie, width=30)
            self.ent_dispo.insert(0, "1") 
            self.ent_dispo.grid(row=4, column=1, padx=5, pady=5)

               # --- ZONE DES BOUTONS ---
            
            self.frame_boutons = tk.Frame(self.tab_livre)
            self.frame_boutons.pack(pady=15)

            
            tk.Button(self.frame_boutons, text="➕ Insérer", bg="#28a745", fg="white", width=12, command=self.inserer_livre).grid(row=0, column=0, padx=5)
            tk.Button(self.frame_boutons, text="📝 Modifier", bg="#ffc107", width=12, command=self.modifier_livre).grid(row=0, column=1, padx=5)
            tk.Button(self.frame_boutons, text="🗑️ Supprimer", bg="#dc3545", fg="white", width=12, command=self.supprimer_livre).grid(row=0, column=2, padx=5)
            tk.Button(self.frame_boutons, text="🔍 Rechercher", bg="#17a2b8", fg="white", width=12, command=self.rechercher_livre).grid(row=0, column=3, padx=5)
            
           
            self.btn_actualiser = tk.Button(self.frame_boutons, text="🔄 Actualiser", bg="#6c757d", fg="white", width=12, command=self.actualiser_champs_livre)
            self.btn_actualiser.grid(row=0, column=4, padx=5)

            
                # Conteneur pour le tableau
            frame_liste = tk.Frame(self.tab_livre)
            frame_liste.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

            # Définition des colonnes
            colonnes = ("id", "nom", "prenom", "adresse", "telephone", "email", "date")
            self.arbre_livre = ttk.Treeview(frame_liste, columns=colonnes, show="headings")

            
            self.arbre_livre.heading("id", text="ID")
            self.arbre_livre.heading("nom", text="Titre")
            self.arbre_livre.heading("prenom", text="Auteur")
            self.arbre_livre.heading("adresse", text="Année_Publication")
            self.arbre_livre.heading("telephone", text="Catégorie")
            self.arbre_livre.heading("email", text="Disponible")
            self.arbre_livre.heading("date", text="Date Inscription")

            
            self.arbre_livre.column("id", width=50)
            self.arbre_livre.column("nom", width=100)
            self.arbre_livre.column("prenom", width=100)
            
            self.arbre_livre.pack(fill=tk.BOTH, expand=True)

            
            self.afficher_livres()

            self.arbre_livre.bind("<Double-1>", self.selectionner_livre)

            
       
        def inserer_livre(self):
            t, a, g, an, d = self.ent_titre.get(), self.ent_auteur.get(), self.ent_genre.get(), self.ent_annee.get(),self.ent_dispo.get()
    
            if t == "" or a == "":
                messagebox.showwarning("Erreur", "Veuillez remplir au moins le Titre et l'Auteur")
                return
            
            try:
                db = self.connecter_db()
                cursor = db.cursor()
                cursor.execute("INSERT INTO livre (titre, auteur, categorie, annee_publication, disponible) VALUES (%s, %s, %s, %s,%s)", (t, a, g, an, d))
                db.commit()
                messagebox.showinfo("Succès", "Livre ajouté !")
                db.close()
            except Exception as e:
                messagebox.showerror("Erreur", str(e))

        def supprimer_livre(self):
            t = self.ent_titre.get()
            if t == "":
                messagebox.showwarning("Erreur", "Entrez le titre du livre à supprimer")
                return
                
            confirmation = messagebox.askyesno("Confirmation", f"Voulez-vous vraiment supprimer '{t}' ?")
            if confirmation:
                try:
                    db = self.connecter_db()
                    cursor = db.cursor()
                    cursor.execute("DELETE FROM livre WHERE titre = %s", (t,))
                    db.commit()
                    messagebox.showinfo("Succès", "Livre supprimé")
                    db.close()
                except Exception as e:
                    messagebox.showerror("Erreur", str(e))

        def modifier_livre(self):
            t, a, g,an,d = self.ent_titre.get(), self.ent_auteur.get(), self.ent_genre.get(), self.ent_annee.get(), self.ent_dispo.get()
            if t == "" or a == "":
                messagebox.showwarning("Erreur", "Veuillez modifier au moins le Titre ou l'Auteur")
                return
             
            if not hasattr(self, 'current_id') or self.current_id is None:
                messagebox.showwarning("Erreur", "Veuillez d'abord rechercher ou sélectionner un livre")
                return   
            
            try:
                    db = self.connecter_db()
                    cursor = db.cursor()

                    
                    sql = "UPDATE livre SET titre = %s, auteur = %s, categorie = %s, annee_publication = %s, disponible = %s WHERE id_Livre = %s"

                    
                    id_du_livre = self.current_id 

                    
                    valeurs = (t, a, g, an, d, int(self.current_id)) 

                    cursor.execute(sql, valeurs)
                    
                   
                    if cursor.rowcount > 0:
                        db.commit()
                        messagebox.showinfo("Succès", "Livre modifié avec succès !")
                    else:
                        messagebox.showwarning("Attention", "Aucun livre trouvé avec cet ID.")

                    db.close()

            except Exception as e:
                    messagebox.showerror("Erreur", str(e))
        def rechercher_livre(self):
            criteres = {
                "titre": self.ent_titre.get().strip(),
                "auteur": self.ent_auteur.get().strip(),
                "annee_publication": self.ent_annee.get().strip(),
                "categorie": self.ent_genre.get().strip(),
                "disponible": self.ent_dispo.get().strip(),
               
            }

            filtres = []
            valeurs = []
            for nom_colonne, valeur_saisie in criteres.items():
                if valeur_saisie != "":
                    filtres.append(f"{nom_colonne} = %s")
                    valeurs.append(valeur_saisie)
            
            if not filtres:
                messagebox.showwarning("Attention", "Veuillez remplir au moins un champ pour rechercher.")
                return
                # --- LOGIQUE DE MISE À JOUR DE L'INTERFACE ---
            
            for item in self.arbre_livre.get_children():
                self.arbre_livre.delete(item)

            try:
                db = self.connecter_db()
               
                cursor = db.cursor()
                
                requete_sql = "SELECT id_Livre, titre, auteur, categorie, annee_publication, disponible, date_inscription FROM livre WHERE " + " AND ".join(filtres)
                
                cursor.execute(requete_sql, valeurs)
                resultat = cursor.fetchall() 

                if resultat:
                    self.current_id = resultat[0] 
                    
                    for ligne in resultat:
                        self.arbre_livre.insert("", tk.END, values=ligne)
                    premier = resultat[0] 
                    self.current_id = premier[0] 
                    
                    
                    self.ent_titre.delete(0, tk.END)
                    self.ent_titre.insert(0, premier[1] or "") 
                    self.ent_auteur.delete(0, tk.END)
                    self.ent_auteur.insert(0, premier[2] or "")
                    self.ent_annee.delete(0, tk.END)
                    self.ent_annee.insert(0, premier[3] or "")
                    self.ent_genre.delete(0, tk.END)
                    self.ent_genre.insert(0, premier[4] or "")
                    self.ent_dispo.delete(0, tk.END)
                    self.ent_dispo.insert(0, premier[5] or "")
                    

                    messagebox.showinfo("Succès", f"{len(resultat)} livre(s) trouvé(s) !")
                else:
                    messagebox.showwarning("Introuvable", "Aucun livre ne correspond.")
                    
                cursor.close() 
                db.close()
            except Exception as e:
                messagebox.showerror("Erreur SQL", f"Détails : {str(e)}")

        def actualiser_champs_livre(self):
           
            self.ent_titre.delete(0, tk.END)
            self.ent_auteur.delete(0, tk.END)
            self.ent_genre.delete(0, tk.END)
            self.ent_annee.delete(0, tk.END)
            self.ent_dispo.delete(0, tk.END)
            
            if hasattr(self, 'ent_date'): 
                 self.ent_date.delete(0, tk.END)

           
            
            self.afficher_livres()
        
        def afficher_livres(self):
           
            for item in self.arbre_livre.get_children():
                self.arbre_livre.delete(item)
            conn = None 
           
            try:
                conn = self.connecter_db()
                curseur = conn.cursor()
               
                curseur.execute("SELECT id_Livre, titre, auteur, annee_publication, categorie, disponible, date_inscription FROM livre")
                lignes = curseur.fetchall()

                for ligne in lignes:
                    self.arbre_livre.insert("", tk.END, values=ligne)
                curseur.close()
                conn.close()
            except pymysql.MySQLError as err: 
               messagebox.showerror("Erreur SQL", f"Impossible de lire les livres : {err}")
            
            finally:
              
                if conn and conn.open:
                    conn.close()
                

        def selectionner_livre(self, event):
             
            selection = self.arbre_livre.selection()
           
            if selection:
                item_selectionne = selection[0]
                valeurs = self.arbre_livre.item(item_selectionne, 'values')
                if valeurs:
                    
                    self.ent_titre.delete(0, tk.END)
                    self.ent_auteur.delete(0, tk.END)
                    self.ent_genre.delete(0, tk.END)
                    self.ent_annee.delete(0, tk.END)
                    self.ent_dispo.delete(0, tk.END)

                   
                    self.ent_titre.insert(0, valeurs[1]) 
                    self.ent_auteur.insert(0, valeurs[2])
                    self.ent_annee.insert(0, valeurs[3]) 
                    self.ent_genre.insert(0, valeurs[4]) 
                    self.ent_dispo.insert(0, valeurs[5])

                    
                    self.current_id = valeurs[0]
            
                        
            else:
            
                print("Clic dans le vide (aucune ligne sélectionnée)")

            
         
        def construire_tab_emprunt(self):
            
            tk.Label(self.tab_emprunt, text="Gestion des emprunts", font=("Arial", 14)).pack(pady=10)
            

             
                # --- ZONE DE SAISIE (Frame) ---
            frame_saisie = tk.Frame(self.tab_emprunt)
            frame_saisie.pack(pady=10)

            tk.Label(frame_saisie, text="Num_abonné :").grid(row=0, column=0, padx=5, pady=5)
            self.ent_titre1= tk.Entry(frame_saisie, width=30)
            self.ent_titre1.grid(row=0, column=1, padx=5, pady=5)

            tk.Label(frame_saisie, text="Num_livre :").grid(row=1, column=0, padx=5, pady=5)
            self.ent_auteur1 = tk.Entry(frame_saisie, width=30)
            self.ent_auteur1.grid(row=1, column=1, padx=5, pady=5)

            
            tk.Label(frame_saisie, text="Date_retour AAAA/MM/JJ:").grid(row=2, column=0, padx=5, pady=5)
            self.ent_annee1 = tk.Entry(frame_saisie, width=30)
            self.ent_annee1.grid(row=2, column=1, padx=5, pady=5)

            tk.Label(frame_saisie, text="Date_limite AAAA/MM/JJ :").grid(row=3, column=0, padx=5, pady=5)
            self.ent_dispo1 = tk.Entry(frame_saisie, width=30)
            self.ent_dispo1.grid(row=3, column=1, padx=5, pady=5)


              # --- ZONE DES BOUTONS ---
            
            self.frame_boutons = tk.Frame(self.tab_emprunt)
            self.frame_boutons.pack(pady=15)

            
            tk.Button(self.frame_boutons, text="➕ Insérer", bg="#28a745", fg="white", width=12, command=self.inserer_emprunt).grid(row=0, column=0, padx=5)
            tk.Button(self.frame_boutons, text="📝 Modifier", bg="#ffc107", width=12, command=self.modifier_emprunt).grid(row=0, column=1, padx=5)
            tk.Button(self.frame_boutons, text="🗑️ Supprimer", bg="#dc3545", fg="white", width=12, command=self.supprimer_emprunt).grid(row=0, column=2, padx=5)
            tk.Button(self.frame_boutons, text="🔍 Rechercher", bg="#17a2b8", fg="white", width=12, command=self.rechercher_emprunt).grid(row=0, column=3, padx=5)
            
            
            self.btn_actualiser = tk.Button(self.frame_boutons, text="🔄 Actualiser", bg="#6c757d", fg="white", width=12, command=self.actualiser_champs_emprunt)
            self.btn_actualiser.grid(row=0, column=4, padx=5)

             
            frame_liste = tk.Frame(self.tab_emprunt)
            frame_liste.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

            
            colonnes = ("id", "nom", "prenom", "adresse", "telephone", "email", "date")
            self.arbre_emprunt = ttk.Treeview(frame_liste, columns=colonnes, show="headings")

           
            self.arbre_emprunt.heading("id", text="ID")
            self.arbre_emprunt.heading("nom", text="Num_Abonné")
            self.arbre_emprunt.heading("prenom", text="Num_Livre")
            self.arbre_emprunt.heading("adresse", text="Date_Emprunt")
            self.arbre_emprunt.heading("telephone", text="Date_Retour")
            self.arbre_emprunt.heading("email", text="Date_Limite")
            
            
            self.arbre_emprunt.column("id", width=50)
            self.arbre_emprunt.column("nom", width=100)
            self.arbre_emprunt.column("prenom", width=100)
            
            self.arbre_emprunt.pack(fill=tk.BOTH, expand=True)

            
            self.afficher_emprunts()

            self.arbre_emprunt.bind("<Double-1>", self.selectionner_emprunt)

            
       

        def inserer_emprunt(self):
            t, a, an, d = self.ent_titre1.get(), self.ent_auteur1.get(), self.ent_annee1.get(),self.ent_dispo1.get()
    
            if t == "" or a == "":
                messagebox.showwarning("Erreur", "Veuillez remplir au moins une case")
                return
            
            try:
                db = self.connecter_db()
                cursor = db.cursor()
                cursor.execute("INSERT INTO emprunt (id_abonne, id_Livre, date_retour, date_limite) VALUES (%s, %s, %s,%s)", (t, a, an, d))
                db.commit()
                messagebox.showinfo("Succès", " Emprunt enregistré avec succès !")
                db.close()
            except Exception as e:
                messagebox.showerror("Erreur", str(e))

        def supprimer_emprunt(self):
            t = self.ent_titre1.get()
            if t == "":
                messagebox.showwarning("Erreur", "Entrez le numero de l'abonné à supprimer")
                return
                
            confirmation = messagebox.askyesno("Confirmation", f"Voulez-vous vraiment supprimer '{t}' ?")
            if confirmation:
                try:
                    db = self.connecter_db()
                    cursor = db.cursor()
                    cursor.execute("DELETE FROM emprunt WHERE id_abonne = %s", (t,))
                    db.commit()
                    messagebox.showinfo("Succès", "Emprunt supprimé")
                    db.close()
                except Exception as e:
                    messagebox.showerror("Erreur", str(e))

        def modifier_emprunt(self):
            t, a, an, d = self.ent_titre1.get(), self.ent_auteur1.get(), self.ent_annee1.get(), self.ent_dispo1.get()
            if t == "" or a == "":
                messagebox.showwarning("Erreur", "Veuillez modifier au moins une case")
                return
            if not hasattr(self, 'current_id') or self.current_id is None:
                messagebox.showwarning("Erreur", "Veuillez d'abord rechercher ou sélectionner un livre")
                return     
            
            try:
                db = self.connecter_db()
                cursor = db.cursor()
               
                    
                sql = "UPDATE emprunt SET id_abonne = %s, id_Livre = %s, date_retour = %s, date_limite = %s  WHERE id_emprunt = %s"

                
                id_de_emprunt = self.current_id

              
                valeurs = (t, a, an, d, int(self.current_id)) 

                cursor.execute(sql, valeurs)
                    
                   
                if cursor.rowcount > 0:
                   db.commit()
                   messagebox.showinfo("Succès", "Emprunt modifié avec succès !")
                else:
                     messagebox.showwarning("Attention", "Aucun emprunt trouvé avec cet ID.")

                db.close()
            except Exception as e:
                messagebox.showerror("Erreur", str(e))

        def rechercher_emprunt(self):
            criteres = {
                "id_abonne": self.ent_titre1.get().strip(),
                "id_Livre": self.ent_auteur1.get().strip(),
                "date_retour": self.ent_annee1.get().strip(),
                "date_limite": self.ent_dispo1.get().strip(),
               
            }

            filtres = []
            valeurs = []
            for nom_colonne, valeur_saisie in criteres.items():
                if valeur_saisie != "":
                    filtres.append(f"{nom_colonne} = %s")
                    valeurs.append(valeur_saisie)
            
            if not filtres:
                messagebox.showwarning("Attention", "Veuillez remplir au moins un champ pour rechercher.")
                return
                # --- LOGIQUE DE MISE À JOUR DE L'INTERFACE ---
            
            for item in self.arbre_emprunt.get_children():
                self.arbre_emprunt.delete(item)

            try:
                db = self.connecter_db()
                
                cursor = db.cursor()
                
                requete_sql = "SELECT id_emprunt, id_abonne, id_Livre, date_emprunt, date_retour, date_limite  FROM emprunt WHERE " + " AND ".join(filtres)
                
                cursor.execute(requete_sql, valeurs)
                resultat = cursor.fetchall() 

                if resultat:
                    self.current_id = resultat[0] 
                    
                    for ligne in resultat:
                        self.arbre_emprunt.insert("", tk.END, values=ligne)
                    premier = resultat[0] 
                    self.current_id = premier[0] 
                   
                    
                    self.ent_titre1.delete(0, tk.END)
                    self.ent_titre1.insert(0, premier[1] or "") 
                    self.ent_auteur1.delete(0, tk.END)
                    self.ent_auteur1.insert(0, premier[2] or "")
                    self.ent_annee1.delete(0, tk.END)
                    self.ent_annee1.insert(0, premier[4] or "")
                    self.ent_dispo1.delete(0, tk.END)
                    self.ent_dispo1.insert(0, premier[5] or "")
                    

                    messagebox.showinfo("Succès", f"{len(resultat)} emprunt(s) trouvé(s) !")
                else:
                    messagebox.showwarning("Introuvable", "Aucun emprunt ne correspond.")
                    
                cursor.close()
                db.close()
            except Exception as e:
                messagebox.showerror("Erreur SQL", f"Détails : {str(e)}")

        def actualiser_champs_emprunt(self):
            
            self.ent_titre1.delete(0, tk.END)
            self.ent_auteur1.delete(0, tk.END)
            self.ent_annee1.delete(0, tk.END)
            self.ent_dispo1.delete(0, tk.END)
            
            if hasattr(self, 'ent_date'): 
                 self.ent_date.delete(0, tk.END)

            
            
            self.afficher_emprunts()
        
        def afficher_emprunts(self):
           
            for item in self.arbre_emprunt.get_children():
                self.arbre_emprunt.delete(item)

            
            try:
                conn = self.connecter_db()
                curseur = conn.cursor()
                
                curseur.execute("SELECT id_emprunt, id_abonne, id_Livre, date_emprunt, date_retour, date_limite FROM emprunt")
                lignes = curseur.fetchall()

                for ligne in lignes:
                    self.arbre_emprunt.insert("", tk.END, values=ligne)
                curseur.close()
                conn.close()
            except pymysql.connect.Error as err:
                print(f"Erreur SQL : {err}")
            
            finally:
                
                if conn and conn.open:
                    conn.close()    

        def selectionner_emprunt(self, event):
            
            selection = self.arbre_emprunt.selection()
            
            if selection:
                item_selectionne = selection[0]
                valeurs = self.arbre_emprunt.item(item_selectionne, 'values')
                if valeurs:
                   
                    self.ent_titre1.delete(0, tk.END)
                    self.ent_auteur1.delete(0, tk.END)
                    self.ent_annee1.delete(0, tk.END)
                    self.ent_dispo1.delete(0, tk.END)

                    
                    self.ent_titre1.insert(0, valeurs[1]) 
                    self.ent_auteur1.insert(0, valeurs[2])
                    self.ent_annee1.insert(0, valeurs[4])
                    self.ent_dispo1.insert(0, valeurs[5])

                    
                    self.current_id = valeurs[0]
            else:
            
                print("Clic dans le vide (aucune ligne sélectionnée)")

                        
           
            
        def construire_tab_abonne(self):
            
            tk.Label(self.tab_abonne, text="Gestion des abonnés", font=("Arial", 14)).pack(pady=10)
            
              # --- ZONE DE SAISIE (Frame) ---
            frame_saisie = tk.Frame(self.tab_abonne)
            frame_saisie.pack(pady=10)

            tk.Label(frame_saisie, text="Nom de l'abonné :").grid(row=0, column=0, padx=5, pady=5)
            self.ent_titre2 = tk.Entry(frame_saisie, width=30)
            self.ent_titre2.grid(row=0, column=1, padx=5, pady=5)

            tk.Label(frame_saisie, text="Prénom de l'abonné :").grid(row=1, column=0, padx=5, pady=5)
            self.ent_auteur2 = tk.Entry(frame_saisie, width=30)
            self.ent_auteur2.grid(row=1, column=1, padx=5, pady=5)

            tk.Label(frame_saisie, text="Adresse de l'abonné :").grid(row=2, column=0, padx=5, pady=5)
            self.ent_genre2 = tk.Entry(frame_saisie, width=30)
            self.ent_genre2.grid(row=2, column=1, padx=5, pady=5)

            tk.Label(frame_saisie, text="Téléphone de l'abonné :").grid(row=3, column=0, padx=5, pady=5)
            self.ent_annee2 = tk.Entry(frame_saisie, width=30)
            self.ent_annee2.grid(row=3, column=1, padx=5, pady=5)

            tk.Label(frame_saisie, text="Email de l'abonné :").grid(row=4, column=0, padx=5, pady=5)
            self.ent_dispo2 = tk.Entry(frame_saisie, width=30)
            self.ent_dispo2.grid(row=4, column=1, padx=5, pady=5)
            

               # --- ZONE DES BOUTONS ---
            
            self.frame_boutons = tk.Frame(self.tab_abonne)
            self.frame_boutons.pack(pady=15)

            
            tk.Button(self.frame_boutons, text="➕ Insérer", bg="#28a745", fg="white", width=12, command=self.inserer_abonne).grid(row=0, column=0, padx=5)
            tk.Button(self.frame_boutons, text="📝 Modifier", bg="#ffc107", width=12, command=self.modifier_abonne).grid(row=0, column=1, padx=5)
            tk.Button(self.frame_boutons, text="🗑️ Supprimer", bg="#dc3545", fg="white", width=12, command=self.supprimer_abonne).grid(row=0, column=2, padx=5)
            tk.Button(self.frame_boutons, text="🔍 Rechercher", bg="#17a2b8", fg="white", width=12, command=self.rechercher_abonne).grid(row=0, column=3, padx=5)
            
            
            self.btn_actualiser = tk.Button(self.frame_boutons, text="🔄 Actualiser", bg="#6c757d", fg="white", width=12, command=self.actualiser_champs_abonne)
            self.btn_actualiser.grid(row=0, column=4, padx=5)

                
            frame_liste = tk.Frame(self.tab_abonne)
            frame_liste.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

            # Définition des colonnes
            colonnes = ("id", "nom", "prenom", "adresse", "telephone", "email", "date")
            self.arbre_abonne = ttk.Treeview(frame_liste, columns=colonnes, show="headings")

            
            self.arbre_abonne.heading("id", text="ID")
            self.arbre_abonne.heading("nom", text="Nom")
            self.arbre_abonne.heading("prenom", text="Prénom")
            self.arbre_abonne.heading("adresse", text="Adresse")
            self.arbre_abonne.heading("telephone", text="Téléphone")
            self.arbre_abonne.heading("email", text="Email")
            self.arbre_abonne.heading("date", text="Date Inscription")

            
            self.arbre_abonne.column("id", width=50)
            self.arbre_abonne.column("nom", width=100)
            self.arbre_abonne.column("prenom", width=100)
            
            self.arbre_abonne.pack(fill=tk.BOTH, expand=True)

            
            self.afficher_abonnes()

            self.arbre_abonne.bind("<Double-1>", self.selectionner_abonne)

            
       
        def inserer_abonne(self):
            t, a, g, an, d = self.ent_titre2.get(), self.ent_auteur2.get(), self.ent_genre2.get(), self.ent_annee2.get(),self.ent_dispo2.get()
    
            if t == "" or a == "":
                messagebox.showwarning("Erreur", "Veuillez remplir au moins une case")
                return
            
            try:
                db = self.connecter_db()
                cursor = db.cursor()
                cursor.execute("INSERT INTO abonne (nom, prenom, adresse, tel, email) VALUES (%s, %s, %s, %s, %s)", (t, a, g, an, d))
                db.commit()
                messagebox.showinfo("Succès", "Abonné ajouté !")
                db.close()
            except Exception as e:
                messagebox.showerror("Erreur", str(e))

        def supprimer_abonne(self):
            t = self.ent_titre2.get()
            if t == "":
                messagebox.showwarning("Erreur", "Entrez l'abonne à supprimer")
                return
                
            confirmation = messagebox.askyesno("Confirmation", f"Voulez-vous vraiment supprimer '{t}' ?")
            if confirmation:
                try:
                    db = self.connecter_db()
                    cursor = db.cursor()
                    cursor.execute("DELETE FROM abonne WHERE nom = %s", (t,))
                    db.commit()
                    messagebox.showinfo("Succès", "Abonné supprimé")
                    db.close()
                except Exception as e:
                    messagebox.showerror("Erreur", str(e))

        def modifier_abonne(self):
            t, a, g, an, d = self.ent_titre2.get(), self.ent_auteur2.get(), self.ent_genre2.get(), self.ent_annee2.get(), self.ent_dispo2.get()
            if t == "" or a == "":
                messagebox.showwarning("Erreur", "Veuillez modifier au moins une case")
                return
            if not hasattr(self, 'current_id') or self.current_id is None:
                messagebox.showwarning("Erreur", "Veuillez d'abord rechercher ou sélectionner un livre")
                return   
            
            
            try:
                db = self.connecter_db()
                cursor = db.cursor()
                
                    
                sql = "UPDATE abonne SET nom = %s, prenom = %s, adresse = %s, tel = %s, email = %s WHERE id_abonne = %s"

                
                id_de_abonne = self.current_id

                
                valeurs = (t, a, g, an, d, int(self.current_id)) 

                cursor.execute(sql, valeurs)
                    
                   
                if cursor.rowcount > 0:
                        db.commit()
                        messagebox.showinfo("Succès", "Abonné modifié avec succès !")
                else:
                        messagebox.showwarning("Attention", "Aucun abonné trouvé avec cet ID.")

                db.close()
            except Exception as e:
                messagebox.showerror("Erreur", str(e))

        def rechercher_abonne(self):
            criteres = {
                "nom": self.ent_titre2.get().strip(),
                "prenom": self.ent_auteur2.get().strip(),
                "adresse": self.ent_genre2.get().strip(),
                "tel": self.ent_annee2.get().strip(),
                "email": self.ent_dispo2.get().strip(),
               
            }

            filtres = []
            valeurs = []
            for nom_colonne, valeur_saisie in criteres.items():
                if valeur_saisie != "":
                    filtres.append(f"{nom_colonne} = %s")
                    valeurs.append(valeur_saisie)
            
            if not filtres:
                messagebox.showwarning("Attention", "Veuillez remplir au moins un champ pour rechercher.")
                return
                # --- LOGIQUE DE MISE À JOUR DE L'INTERFACE ---
           
            for item in self.arbre_abonne.get_children():
                self.arbre_abonne.delete(item)

            try:
                db = self.connecter_db()
                
                cursor = db.cursor()
                
                requete_sql = "SELECT id_abonne, nom, prenom, adresse, tel, email, date_inscription FROM abonne WHERE " + " AND ".join(filtres)
                
                cursor.execute(requete_sql, valeurs)
                resultat = cursor.fetchall() 

                if resultat:
                    self.current_id = resultat[0]   
                    
                    for ligne in resultat:
                        self.arbre_abonne.insert("", tk.END, values=ligne)
                    premier = resultat[0] 
                    self.current_id = premier[0] 
                    
                    
                    self.ent_titre2.delete(0, tk.END)
                    self.ent_titre2.insert(0, premier[1] or "") 
                    self.ent_auteur2.delete(0, tk.END)
                    self.ent_auteur2.insert(0, premier[2] or "")
                    self.ent_genre2.delete(0, tk.END)
                    self.ent_genre2.insert(0, premier[3] or "")
                    self.ent_annee2.delete(0, tk.END)
                    self.ent_annee2.insert(0, premier[4] or "")
                    self.ent_dispo2.delete(0, tk.END)
                    self.ent_dispo2.insert(0, premier[5] or "")
                    

                    messagebox.showinfo("Succès", f"{len(resultat)} abonné(s) trouvé(s) !")
                else:
                    messagebox.showwarning("Introuvable", "Aucun abonné ne correspond.")
                    
                cursor.close() 
                db.close()
            except Exception as e:
                messagebox.showerror("Erreur SQL", f"Détails : {str(e)}")

        def actualiser_champs_abonne(self):
            
            self.ent_titre2.delete(0, tk.END)
            self.ent_auteur2.delete(0, tk.END)
            self.ent_genre2.delete(0, tk.END)
            self.ent_annee2.delete(0, tk.END)
            self.ent_dispo2.delete(0, tk.END)
            
            if hasattr(self, 'ent_date'): 
                 self.ent_date.delete(0, tk.END)

           
            
            self.afficher_abonnes()
        
        def afficher_abonnes(self):
            
            for item in self.arbre_abonne.get_children():
                self.arbre_abonne.delete(item)

            
            try:
                conn = self.connecter_db()
                curseur = conn.cursor()
               
                curseur.execute("SELECT id_abonne, nom, prenom, adresse, tel, email, date_inscription FROM abonne")
                lignes = curseur.fetchall()

                for ligne in lignes:
                    self.arbre_abonne.insert("", tk.END, values=ligne)
                curseur.close()
                conn.close()
            except pymysql.connect.Error as err:
                print(f"Erreur SQL : {err}")
            
            finally:
               
                if conn and conn.open:
                    conn.close()    

        def selectionner_abonne(self, event):
            
            selection = self.arbre_abonne.selection()
           
            if selection:
                item_selectionne = selection[0]
                valeurs = self.arbre_abonne.item(item_selectionne, 'values')
                if valeurs:
                   
                    self.ent_titre2.delete(0, tk.END)
                    self.ent_auteur2.delete(0, tk.END)
                    self.ent_genre2.delete(0, tk.END)
                    self.ent_annee2.delete(0, tk.END)
                    self.ent_dispo2.delete(0, tk.END)


                    self.ent_titre2.insert(0, valeurs[1]) 
                    self.ent_auteur2.insert(0, valeurs[2])
                    self.ent_genre2.insert(0, valeurs[3])
                    self.ent_annee2.insert(0, valeurs[4])
                    self.ent_dispo2.insert(0, valeurs[5])

                   
                    self.current_id = valeurs[0]
            else:
           
                print("Clic dans le vide (aucune ligne sélectionnée)")

           
            
        def construire_tab_admin(self):
           
            tk.Label(self.tab_admin, text="Gestion des bibliothécaires", font=("Arial", 14)).pack(pady=10)   

            
              # --- ZONE DE SAISIE (Frame) ---
            frame_saisie = tk.Frame(self.tab_admin)
            frame_saisie.pack(pady=10)

            tk.Label(frame_saisie, text="Nom du bibliothécaire :").grid(row=0, column=0, padx=5, pady=5)
            self.ent_titre3 = tk.Entry(frame_saisie, width=30)
            self.ent_titre3.grid(row=0, column=1, padx=5, pady=5)

            tk.Label(frame_saisie, text="Prénom du bibliothécaire :").grid(row=1, column=0, padx=5, pady=5)
            self.ent_auteur3 = tk.Entry(frame_saisie, width=30)
            self.ent_auteur3.grid(row=1, column=1, padx=5, pady=5)

            tk.Label(frame_saisie, text="Email du bibliothécaire :").grid(row=2, column=0, padx=5, pady=5)
            self.ent_genre3 = tk.Entry(frame_saisie, width=30)
            self.ent_genre3.grid(row=2, column=1, padx=5, pady=5)

            tk.Label(frame_saisie, text="Téléphone du bibliothécaire :").grid(row=3, column=0, padx=5, pady=5)
            self.ent_annee3 = tk.Entry(frame_saisie, width=30)
            self.ent_annee3.grid(row=3, column=1, padx=5, pady=5)

            
          
            # --- ZONE DES BOUTONS ---
            
            self.frame_boutons = tk.Frame(self.tab_admin)
            self.frame_boutons.pack(pady=15)

            
            tk.Button(self.frame_boutons, text="➕ Insérer", bg="#28a745", fg="white", width=12, command=self.inserer_admin).grid(row=0, column=0, padx=5)
            tk.Button(self.frame_boutons, text="📝 Modifier", bg="#ffc107", width=12, command=self.modifier_admin).grid(row=0, column=1, padx=5)
            tk.Button(self.frame_boutons, text="🗑️ Supprimer", bg="#dc3545", fg="white", width=12, command=self.supprimer_admin).grid(row=0, column=2, padx=5)
            tk.Button(self.frame_boutons, text="🔍 Rechercher", bg="#17a2b8", fg="white", width=12, command=self.rechercher_admin).grid(row=0, column=3, padx=5)
            
            
            self.btn_actualiser = tk.Button(self.frame_boutons, text="🔄 Actualiser", bg="#6c757d", fg="white", width=12, command=self.actualiser_champs_admin)
            self.btn_actualiser.grid(row=0, column=4, padx=5)

               
            frame_liste = tk.Frame(self.tab_admin)
            frame_liste.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

           
            colonnes = ("id", "nom", "prenom", "email", "telephone", "date")
            self.arbre_admin = ttk.Treeview(frame_liste, columns=colonnes, show="headings")

           
            self.arbre_admin.heading("id", text="ID")
            self.arbre_admin.heading("nom", text="Nom")
            self.arbre_admin.heading("prenom", text="Prénom")
            self.arbre_admin.heading("email", text="Email")
            self.arbre_admin.heading("telephone", text="Téléphone")  
            self.arbre_admin.heading("date", text="Date Inscription")

            
            self.arbre_admin.column("id", width=50)
            self.arbre_admin.column("nom", width=100)
            self.arbre_admin.column("prenom", width=100)
            
            self.arbre_admin.pack(fill=tk.BOTH, expand=True)

           
            self.afficher_admins()

            self.arbre_admin.bind("<Double-1>", self.selectionner_admin)
            
       

        def inserer_admin(self):
            t, a, g, an = self.ent_titre3.get(), self.ent_auteur3.get(), self.ent_genre3.get(), self.ent_annee3.get()
    
            if t == "" or a == "":
                messagebox.showwarning("Erreur", "Veuillez remplir au moins une case")
                return
            
            try:
                db = self.connecter_db()
                cursor = db.cursor()
                cursor.execute("INSERT INTO bibliothécaire (nom_Biblio, prenom_Biblio, email_Biblio, tel_Biblio) VALUES (%s, %s, %s, %s)", (t, a, g, an ))
                db.commit()
                messagebox.showinfo("Succès", "Bibliothécaire ajouté !")
                db.close()
            except Exception as e:
                messagebox.showerror("Erreur", str(e))

        def supprimer_admin(self):
            t = self.ent_titre3.get()
            if t == "":
                messagebox.showwarning("Erreur", "Entrez le bibliothécaire à supprimer")
                return
                
            confirmation = messagebox.askyesno("Confirmation", f"Voulez-vous vraiment supprimer '{t}' ?")
            if confirmation:
                try:
                    db = self.connecter_db()
                    cursor = db.cursor()
                    cursor.execute("DELETE FROM bibliothécaire WHERE nom_Biblio = %s", (t,))
                    db.commit()
                    messagebox.showinfo("Succès", "Bibliothécaire supprimé")
                    db.close()
                except Exception as e:
                    messagebox.showerror("Erreur", str(e))

        def modifier_admin(self):
            t, a, g, an = self.ent_titre3.get(), self.ent_auteur3.get(), self.ent_genre3.get(), self.ent_annee3.get()
            if t == "" or a == "":
                messagebox.showwarning("Erreur", "Veuillez modifier au moins une case")
                return
            if not hasattr(self, 'current_id') or self.current_id is None:
                messagebox.showwarning("Erreur", "Veuillez d'abord rechercher ou sélectionner un livre")
                return   
            
            
            try:
                db = self.connecter_db()
                cursor = db.cursor()
                 
                    
                sql = "UPDATE bibliothécaire SET nom_Biblio = %s, prenom_Biblio = %s, email_Biblio = %s, tel_Biblio = %s  WHERE id_Biblio = %s"

              
                id_de_admin = self.current_id        
                
                valeurs = (t, a, g, an, int(self.current_id)) 

                cursor.execute(sql, valeurs)
                    
                 
                if cursor.rowcount > 0:
                        db.commit()
                        messagebox.showinfo("Succès", "Bibliothècaire modifié avec succès !")
                else:
                        messagebox.showwarning("Attention", "Aucun bibliothècaire trouvé avec cet ID.")

                db.close()
            except Exception as e:
                messagebox.showerror("Erreur", str(e))

        def rechercher_admin(self):
            criteres = {
                "nom_Biblio": self.ent_titre3.get().strip(),
                "prenom_Biblio": self.ent_auteur3.get().strip(),
                "email_Biblio": self.ent_genre3.get().strip(),
                "tel_Biblio": self.ent_annee3.get().strip(),
                
               
            }

            filtres = []
            valeurs = []
            for nom_colonne, valeur_saisie in criteres.items():
                if valeur_saisie != "":
                    filtres.append(f"{nom_colonne} = %s")
                    valeurs.append(valeur_saisie)
            
            if not filtres:
                messagebox.showwarning("Attention", "Veuillez remplir au moins un champ pour rechercher.")
                return
               
           
            for item in self.arbre_admin.get_children():
                self.arbre_admin.delete(item)

            try:
                db = self.connecter_db()
                
                cursor = db.cursor()
                
                requete_sql = "SELECT id_Biblio, nom_Biblio, prenom_Biblio, email_Biblio, tel_Biblio, date_inscription FROM bibliothécaire WHERE " + " AND ".join(filtres)
                
                cursor.execute(requete_sql, valeurs)
                resultat = cursor.fetchall() 

                if resultat:
                    self.current_id = resultat[0]   
                    
                    for ligne in resultat:
                        self.arbre_admin.insert("", tk.END, values=ligne)
                    premier = resultat[0] 
                    self.current_id = premier[0] 
                    
                    
                    self.ent_titre3.delete(0, tk.END)
                    self.ent_titre3.insert(0, premier[1] or "") 
                    self.ent_auteur3.delete(0, tk.END)
                    self.ent_auteur3.insert(0, premier[2] or "")
                    self.ent_genre3.delete(0, tk.END)
                    self.ent_genre3.insert(0, premier[3] or "")
                    self.ent_annee3.delete(0, tk.END)
                    self.ent_annee3.insert(0, premier[4] or "")
                    

                    messagebox.showinfo("Succès", f"{len(resultat)} bibliothécaire(s) trouvé(s) !")
                else:
                    messagebox.showwarning("Introuvable", "Aucun bibliothécaire ne correspond.")
                    
                cursor.close() 
                db.close()
            except Exception as e:
                messagebox.showerror("Erreur SQL", f"Détails : {str(e)}")

        def actualiser_champs_admin(self):
           
            self.ent_titre3.delete(0, tk.END)
            self.ent_auteur3.delete(0, tk.END)
            self.ent_genre3.delete(0, tk.END)
            self.ent_annee3.delete(0, tk.END)
            
            
            if hasattr(self, 'ent_date'): 
                 self.ent_date.delete(0, tk.END)

           
            
            self.afficher_admins()
        
        def afficher_admins(self):
            
            for item in self.arbre_admin.get_children():
                self.arbre_admin.delete(item)

            
            try:
                conn = self.connecter_db()
                curseur = conn.cursor()
                
                curseur.execute("SELECT id_Biblio, nom_Biblio, prenom_Biblio, email_Biblio, tel_Biblio, date_inscription FROM bibliothécaire")
                lignes = curseur.fetchall()

                for ligne in lignes:
                    self.arbre_admin.insert("", tk.END, values=ligne)
                curseur.close()
                conn.close()
            except pymysql.connect.Error as err:
                print(f"Erreur SQL : {err}")
            
            finally:
               
                if conn and conn.open:
                    conn.close()    

        def selectionner_admin(self, event):
           
            selection = self.arbre_admin.selection()
            
            if selection:
                item_selectionne = selection[0]
                valeurs = self.arbre_admin.item(item_selectionne, 'values')
                if valeurs:
                    
                    self.ent_titre3.delete(0, tk.END)
                    self.ent_auteur3.delete(0, tk.END)
                    self.ent_genre3.delete(0, tk.END)
                    self.ent_annee3.delete(0, tk.END)
                    

                    
                    self.ent_titre3.insert(0, valeurs[1]) 
                    self.ent_auteur3.insert(0, valeurs[2])
                    self.ent_genre3.insert(0, valeurs[3])
                    self.ent_annee3.insert(0, valeurs[4])
                    

                   
                    self.current_id = valeurs[0]
            else:
            
                print("Clic dans le vide (aucune ligne sélectionnée)")
if __name__ == "__main__":
    root = tk.Tk()
    app = ApplicationBibliotheque(root)
    root.mainloop()

   
        
 













        

