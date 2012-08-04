require "jsduck/meta_tag"

class PlatformTag < JsDuck::MetaTag
	def initialize
		@name = "platform"
	end
  # This will be called with an array of all @license tags on one class.
  # One can make use of the #format method to easily support
  # Markdown and {@link} tags inside the contents of the tag.
  def to_html(platforms)
    names = {
    	'android' => 'Android',
    	'iphone' => 'iPhone',
    	'ipad' => 'iPad',
    	'mobileweb' => 'Mobile Web'
    }
    "<ul class='platforms'>" + platforms.map{|platform| "<li class='platform-"+platform+"' title='"+names[platform]+"'></li>"}.join("") + "</ul>"
  end
end