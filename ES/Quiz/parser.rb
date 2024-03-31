module IParser
   def initialize (file_path)
      @file_path = file_path
      @data = []
      pattern = /(\d{2}\/\d{7})\s+(.+)/
      matches = File.open(file_path).read.scan(pattern)

      matches.each do |match|
         @data.push({:id => match[0], :name => match[1]})
      end
   end

   def data
      puts "\n
      🎓 SOFTWARE ENGINEERING STUDENTS LIST 🎓\n
      "
      @data.each do |d|
         puts "#{d[:id]}  #{d[:name]}"
      end
   end
end

class Parser
   include IParser
end

# Keeps this section from running when included in another file
if __FILE__ == $0
   file_path = "./engsoft.txt"

   parser = Parser.new(file_path)
   parser.data
end
