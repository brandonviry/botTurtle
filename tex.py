import wx

class ProgressFrame(wx.Frame):
    def __init__(self, parent, title, max_value):
        wx.Frame.__init__(self, parent, title=title)

        # Créer la barre de progression
        self.gauge = wx.Gauge(self, range=max_value)

        # Créer le bouton "Annuler"
        self.cancel_button = wx.Button(self, label="Annuler")
        self.cancel_button.Bind(wx.EVT_BUTTON, self.on_cancel)

        # Créer le gestionnaire de disposition
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.gauge, 0, wx.EXPAND)
        sizer.Add(self.cancel_button, 0, wx.ALIGN_RIGHT)

        self.SetSizer(sizer)
        self.Fit()

    def on_cancel(self, event):
        # Fermer la fenêtre lorsque le bouton "Annuler" est cliqué
        self.Close()
    def update_progress(self,value):
         frame.gauge.SetValue(value)


# Exemple d'utilisation de la fenêtre de progression
app = wx.App()
frame = ProgressFrame(None, "Opération en cours", 100)
frame.Show()

# Mettre à jour la barre de progression à 50%
frame.update_progress(50) 
input()