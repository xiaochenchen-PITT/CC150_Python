import Tkinter as tk

class Observable:
	"""class Observable defines the infrastructure of 
	model/view register and notification"""
	def __init__(self, InitialValue = 0):
		self.data = InitialValue
		self.observer_list = []

	def RegisterObserver(self, observer):
		self.observer_list.append(observer)

	def ObserverNotify(self):
		for ov in self.observer_list:
			ov.update(self.data)

	def get(self):
		return self.data

class Model(Observable):
	"""Model extends its super class Observable and purely just functions"""
	def __init__(self):
		Observable.__init__(self)
		
	def AddMoney(self, value):
		self.data = self.get() + value
		Observable.ObserverNotify(self)

	def SubMoney(self, value):
		self.data = self.get() - value
		Observable.ObserverNotify(self)

class View(tk.Toplevel):
	"""viewis the visual presentation of data"""
	def __init__(self, master):
		tk.Toplevel.__init__(self, master)

		self.up_frame = tk.Frame(self)
		self.up_frame.pack()
		self.bottom_frame = tk.Frame(self)
		self.bottom_frame.pack(side = 'bottom')

		self.label = tk.Label(self.up_frame, text = 'My Money')
		self.label.pack(side = 'left')

		self.moneyDisplay = tk.Entry(self.up_frame, width = 8)
		self.moneyDisplay.pack(side = 'left')

		self.addButton = tk.Button(self.bottom_frame, text = 'Add', width = 8)
		self.addButton.pack(side = 'left')

		self.subButton = tk.Button(self.bottom_frame, text = 'Sub', width = 8)
		self.subButton.pack(side = 'left')

	def update(self, money):
		self.moneyDisplay.delete(0, 'end')
		self.moneyDisplay.insert('end', str(money))

class Controller:
	"""Controller is the interconnection of model and view"""
	def __init__(self, root):
		self.model = Model()
		self.view = View(root)
		self.model.RegisterObserver(self.view)

		self.view.addButton.config(command = self.AddMoney)
		self.view.subButton.config(command = self.SubMoney)
		self.MoneyChanged(self.model.get())

	def AddMoney(self):
		self.model.AddMoney(10)

	def SubMoney(self):
		self.model.SubMoney(10)

	def MoneyChanged(self, money):
		self.view.update(money)


if __name__ == '__main__':
	root = tk.Tk()
	root.withdraw()
	whatever = Controller(root)
	root.mainloop()



		

		