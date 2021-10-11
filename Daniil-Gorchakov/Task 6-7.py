class Pagination():
	def __init__(self, text, chars_on_page):
		self.text = text
		self.chars_on_page = chars_on_page

		self.items = text.split()
		self.items_len = len(self.items)

		self.text_length = len(text)
		self.pages_count = self.text_length % chars_on_page

		self.create_pages()

	def create_pages(self):
		self.page_item = {page:"" for page in range(self.pages_count)}

		start = 0
		end = self.chars_on_page
		for page in range(self.pages_count):
			self.page_item[page] = self.text[start:end]
			start += self.chars_on_page
			end += self.chars_on_page

		self.item_page = {self.page_item[item]:item for item in self.page_item}

	def item_count(self):
		print(self.text_length)

	def page_count(self):
		print(self.pages_count)

	def count_items_on_page(self, page_number):
		if page_number > self.items_len:
			print("Exception: Invalid index. Page is missing.")
		else:
			print(len(self.page_item[page_number]))

	def find_page(self, find):
		result = []
		for item_on_page in self.item_page:
			if find in item_on_page:
				result.append(self.item_page[item_on_page])
			elif item_on_page.replace(" ", "") in find:
				result.append(self.item_page[item_on_page])

		if len(result) == 0:
			print(f"Exception: {find} is missing on the pages")
		else:
			print(result)

	def display_page(self, page_number):
		print(self.page_item[page_number])


if __name__ == "__main__":
	pages = Pagination('Your beautiful text', 5)

	pages.page_count()
	#>>> 4
	pages.item_count()
	#>>> 19

	pages.count_items_on_page(0)
	#>>> 5
	pages.count_items_on_page(3)
	#>>> 4
	pages.count_items_on_page(4)
	#>>> Exception: Invalid index. Page is missing.

	# Optional
	pages.find_page('Your')
	#>>> [0]
	pages.find_page('e')
	#>>> [1, 3]
	pages.find_page('beautiful')
	#>>> [1, 2]
	pages.find_page('great')
	#>>> Exception: 'great' is missing on the pages
	pages.display_page(0)
	#>>> 'Your '
