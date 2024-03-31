require_relative './parser.rb'

class ParserOrdered
	include IParser

	def sorted items
		 items.sort do |a, b|
				yield a, b
		 end
	end

	# sort_by: :id or :name
	def data(sort_by = :name)
		puts "\n
		🎓 SOFTWARE ENGINEERING STUDENTS LIST 🎓
		\n"

		 if sort_by == :id
				ordered = self.sorted(@data) do |a, b|
					 a[:id] <=> b[:id]
				end
		 elsif sort_by == :name
				ordered = self.sorted(@data) do |a, b|
					 a[:name] <=> b[:name]
				end
		 end

		 ordered.each do |d|
				puts "#{d[:id]}  #{d[:name]}"
		 end
	end
end

# Keeps this section from running when included in another file
if __FILE__ == $0
	file_path = "./engsoft.txt"
	# ask user input for sort_by

	parser = ParserOrdered.new(file_path)
	puts "⭐ Default: Sort by name
	\n🔢 Sort by ID? (Y/n)"

	begin
		input = gets.chomp
	rescue Interrupt
		puts "\nInput interrupted. Exiting..."
		exit
	end

	if input == "Y" || input == "y"
		parser.data(:id)
	else
		parser.data(:name)
	end
end
