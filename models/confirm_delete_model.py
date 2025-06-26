from app_init import mydb

def delete_user_and_related_data(user_id):
    try:
        cursor = mydb.cursor()

        # Supprimer les dépendances (ex : LIKED)
        cursor.execute("DELETE FROM LIKED WHERE idUser = %s", (user_id,))

        # Supprimer l'utilisateur
        cursor.execute("DELETE FROM USER WHERE idUser = %s", (user_id,))

        mydb.commit()
        return True, "Compte supprimé avec succès."

    except Exception as e:
        print("Erreur lors de la suppression de compte:", e)
        return False, "Erreur serveur lors de la suppression du compte."
