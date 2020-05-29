"""
	                                      __     
	                                     /\ \    
	 __  __  __    ___   ____     ___    \_\ \   
	/\ \/\ \/\ \  / __`\/\_ ,`\  / __`\  /'_` \  
	\ \ \_/ \_/ \/\ \L\ \/_/  /_/\ \L\ \/\ \L\ \ 
	 \ \___x___/'\ \____/ /\____\ \____/\ \___,_\
	  \/__//__/   \/___/  \/____/\/___/  \/__,_ /
	                                             
	                                             
	
	- Bueno, pues este programa lo que hace es crear un banner con comentarios.
	- Espero que os guste la idea, gracias y disfrutarlo ;D.
	- Introduce primero el archivo al que quieres aplicar el banner.
  	- Introduce el archivo final de salida para el banner, puedes usar el mismo o crear uno nuevo, como desees.
  	- Después simplemente pones la fuente y si lo deseas le agregas comentarios a tu codigo.
  	- Diviertete ;D
"""
import os
import pyfiglet
from pyfiglet import Figlet
fonts = ['1943____.flf', '1row', '3-d', '3d_diagonal', '3x5', '4max', '4x4_offr', '5lineoblique', '5x7', '5x8', '64f1____', '6x10', '6x9', 'B1FF', 'DANC4', 'ICL-1900', 'a_zooloo', 'acrobatic', 'advenger', 'alligator', 'alligator2', 'alligator3', 'alpha', 'alphabet', 'amc3line', 'amc3liv1', 'amcaaa01', 'amcneko', 'amcrazo2', 'amcrazor', 'amcslash', 'amcslder', 'amcthin', 'amctubes', 'amcun1', 'aquaplan', 'arrows', 'asc_____', 'ascii___', 'ascii_new_roman', 'assalt_m', 'asslt__m', 'atc_____', 'atc_gran', 'avatar', 'b_m__200', 'banner', 'banner3-D', 'banner3', 'banner4', 'barbwire', 'basic', 'battle_s', 'battlesh', 'baz__bil', 'bear', 'beer_pub', 'bell', 'benjamin', 'big', 'bigchief', 'bigfig', 'binary', 'block', 'blocks', 'bolger', 'braced', 'bright', 'brite', 'briteb', 'britebi', 'britei', 'broadway', 'broadway_kb', 'bubble', 'bubble__', 'bubble_b', 'bulbhead', 'c1______', 'c2______', 'c_ascii_', 'c_consen', 'calgphy2', 'caligraphy', 'cards', 'catwalk', 'caus_in_', 'char1___', 'char2___', 'char3___', 'char4___', 'charact1', 'charact2', 'charact3', 'charact4', 'charact5', 'charact6', 'characte', 'charset_', 'chartr', 'chartri', 'chiseled', 'chunky', 'clb6x10', 'clb8x10', 'clb8x8', 'cli8x8', 'clr4x6', 'clr5x10', 'clr5x6', 'clr5x8', 'clr6x10', 'clr6x6', 'clr6x8', 'clr7x10', 'clr7x8', 'clr8x10', 'clr8x8', 'coil_cop', 'coinstak', 'cola', 'colossal', 'com_sen_', 'computer', 'contessa', 'contrast', 'convoy__', 'cosmic', 'cosmike', 'cour', 'courb', 'courbi', 'couri', 'crawford', 'crazy', 'cricket', 'cursive', 'cyberlarge', 'cybermedium', 'cybersmall', 'cygnet', 'd_dragon', 'dancingfont', 'dcs_bfmo', 'decimal', 'deep_str', 'defleppard', 'demo_1__', 'demo_2__', 'demo_m__', 'devilish', 'diamond', 'dietcola', 'digital', 'doh', 'doom', 'dosrebel', 'dotmatrix', 'double', 'doubleshorts', 'drpepper', 'druid___', 'dwhistled', 'e__fist_', 'ebbs_1__', 'ebbs_2__', 'eca_____', 'eftichess', 'eftifont', 'eftipiti', 'eftirobot', 'eftitalic', 'eftiwall', 'eftiwater', 'epic', 'etcrvs__', 'f15_____', 'faces_of', 'fair_mea', 'fairligh', 'fantasy_', 'fbr12___', 'fbr1____', 'fbr2____', 'fbr_stri', 'fbr_tilt', 'fender', 'filter', 'finalass', 'fire_font-k', 'fire_font-s', 'fireing_', 'flipped', 'flowerpower', 'flyn_sh', 'fourtops', 'fp1_____', 'fp2_____', 'fraktur', 'funface', 'funfaces', 'funky_dr', 'future_1', 'future_2', 'future_3', 'future_4', 'future_5', 'future_6', 'future_7', 'future_8', 'fuzzy', 'gauntlet', 'georgi16', 'georgia11', 'ghost', 'ghost_bo', 'ghoulish', 'glenyn', 'goofy', 'gothic', 'gothic__', 'graceful', 'gradient', 'graffiti', 'grand_pr', 'greek', 'green_be', 'hades___', 'heart_left', 'heart_right', 'heavy_me', 'helv', 'helvb', 'helvbi', 'helvi', 'henry3d', 'heroboti', 'hex', 'hieroglyphs', 'high_noo', 'hills___', 'hollywood', 'home_pak', 'horizontalleft', 'horizontalright', 'house_of', 'hypa_bal', 'hyper___', 'impossible', 'inc_raw_', 'invita', 'isometric1', 'isometric2', 'isometric3', 'isometric4', 'italic', 'italics_', 'ivrit', 'jacky', 'jazmine', 'jerusalem', 'joust___', 'katakana', 'kban', 'keyboard', 'kgames_i', 'kik_star', 'knob', 'konto', 'kontoslant', 'krak_out', 'larry3d', 'lazy_jon', 'lcd', 'lean', 'letter_w', 'letters', 'letterw3', 'lexible_', 'lildevil', 'lineblocks', 'linux', 'lockergnome', 'mad_nurs', 'madrid', 'magic_ma', 'marquee', 'master_o', 'maxfour', 'mayhem_d', 'mcg_____', 'merlin1', 'merlin2', 'mig_ally', 'mike', 'mini', 'mirror', 'mnemonic', 'modern__', 'modular', 'morse', 'morse2', 'moscow', 'mshebrew210', 'muzzle', 'nancyj-fancy', 'nancyj-improved', 'nancyj-underlined', 'nancyj', 'new_asci', 'nfi1____', 'nipples', 'notie_ca', 'npn_____', 'nscript', 'ntgreek', 'nvscript', 'o8', 'octal', 'odel_lak', 'ogre', 'ok_beer_', 'oldbanner', 'os2', 'outrun__', 'p_s_h_m_', 'p_skateb', 'pacos_pe', 'panther_', 'pawn_ins', 'pawp', 'peaks', 'peaksslant', 'pebbles', 'pepper', 'phonix__', 'platoon2', 'platoon_', 'pod_____', 'poison', 'puffy', 'puzzle', 'pyramid', 'r2-d2___', 'rad_____', 'rad_phan', 'radical_', 'rainbow_', 'rally_s2', 'rally_sp', 'rammstein', 'rampage_', 'rastan__', 'raw_recu', 'rci_____', 'rectangles', 'red_phoenix', 'relief', 'relief2', 'rev', 'reverse', 'ripper!_', 'road_rai', 'rockbox_', 'rok_____', 'roman', 'roman___', 'rot13', 'rotated', 'rounded', 'rowancap', 'rozzo', 'runic', 'runyc', 's-relief', 'sans', 'sansb', 'sansbi', 'sansi', 'santaclara', 'sblood', 'sbook', 'sbookb', 'sbookbi', 'sbooki', 'script', 'script__', 'serifcap', 'shadow', 'shimrod', 'short', 'skate_ro', 'skateord', 'skateroc', 'sketch_s', 'slant', 'slide', 'slscript', 'sm______', 'small', 'smallcaps', 'smisome1', 'smkeyboard', 'smpoison', 'smscript', 'smshadow', 'smslant', 'smtengwar', 'soft', 'space_op', 'spc_demo', 'speed', 'spliff', 'stacey', 'stampate', 'stampatello', 'standard', 'star_war', 'starstrips', 'starwars', 'stealth_', 'stellar', 'stencil1', 'stencil2', 'stforek', 'stop', 'straight', 'street_s', 'sub-zero', 'subteran', 'super_te', 'swampland', 'swan', 'sweet', 't__of_ap', 'tanja', 'tav1____', 'taxi____', 'tec1____', 'tec_7000', 'tecrvs__', 'tengwar', 'term', 'test1', 'thick', 'thin', 'threepoint', 'ti_pan__', 'ticks', 'ticksslant', 'tiles', 'times', 'timesofl', 'tinker-toy', 'tomahawk', 'tombstone', 'top_duck', 'train', 'trashman', 'trek', 'triad_st', 'ts1_____', 'tsalagi', 'tsm_____', 'tsn_base', 'tty', 'ttyb', 'tubular', 'twin_cob', 'twisted', 'twopoint', 'type_set', 'ucf_fan_', 'ugalympi', 'unarmed_', 'univers', 'usa_____', 'usa_pq__', 'usaflag', 'utopia', 'utopiab', 'utopiabi', 'utopiai', 'varsity', 'vortron_', 'war_of_w', 'wavy', 'weird', 'wetletter', 'whimsy', 'wow', 'xbrite', 'xbriteb', 'xbritebi', 'xbritei', 'xchartr', 'xchartri', 'xcour', 'xcourb', 'xcourbi', 'xcouri', 'xhelv', 'xhelvb', 'xhelvbi', 'xhelvi', 'xsans', 'xsansb', 'xsansbi', 'xsansi', 'xsbook', 'xsbookb', 'xsbookbi', 'xsbooki', 'xtimes', 'xtty', 'xttyb', 'yie-ar__', 'yie_ar_k', 'z-pilot_', 'zig_zag_', 'zone7___']
file = input("Escribe el nombre del archivo:\n")
file = open(file,"r")
nfile = input("Escribe el nombre para el nuevo archivo:\n")
if (os.path.isfile(nfile) == True):
	ffile = open(nfile,"r")
else:
	ffile = open(nfile,"w")
archivo = ""
linea = file.readline()
while(linea != ""):
	archivo = archivo + linea
	linea = file.readline()
fuente = input("Escribe la fuente para el banner\n")
if (fuente in fonts):
	comentario = input("Escribe el texto:\n")
	q = Figlet(font=fuente)
	q = q.renderText(comentario)
	q = q.split("\n")
	text = "\"\"\"\n"
	for i in range(len(q)):
		text += "\t{0}\n".format(q[i])
	comentario = input("Deseas añadir una breve explicación o comentario del código ?\n Escribe si o no.\n")
	while(comentario != ""):
		if(comentario.lower() == "si"):
			comentario = input("Escribe el comentario que deseas:\n")
			text += "\t- {0}\n".format(comentario)
			comentario = input("Deseas añadir más comentarios ?\n Escribe si o no.\n")
			while(comentario.lower == "si"):
				text += "\t- {0}\n".format(comentario)
				comentario = input("Deseas añadir más comentarios ?\n Escribe si o no.\n")
		else:
			break
	text += "\"\"\"\n"
	text += "{0}\n".format(archivo)
	text = text.split("\n")
else:
	print("La fuente no existe, prueba con otra.")
ffile = open(nfile,"w")
for i in range(len(text)):
	ffile.write("{0}\n".format(text[i]))
file.close()
ffile.close()
