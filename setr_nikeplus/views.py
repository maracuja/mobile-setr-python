from django.shortcuts import render_to_response
from django.conf import settings
from django.core import serializers


def import_runs(request):
	my_runs_url = "http://nikeplus.nike.com/nikeplus/v1/services/widget/get_public_run_list.jsp?userID=%s" % (settings.NIKEPLUS_USERID,) 
	

		$xml = simplexml_load_file($my_runs_url);
		$runs = array();
		foreach ($xml->runList->run as $run) $runs[] = $run;
		$runs = array_reverse($runs);
		
		foreach ($runs as $run)
		{
			$width = (string) $run->distance * 75;
			$date = new DateTime((string) $run->startTime);
			$time = $date->format('H:i');
			$date = $date->format('Y-m-d');
			echo "<li class='run howfelt{$run->howFelt}' style='width: {$width}'>";
			echo round((float) $run->distance, 2) . "km - {$date} {$time} - {$run->equipmentType}";
			// echo " - <a href='" . str_replace("<run-id>", $run->attributes()->id, $gps_data_url) . "'>gps</a>";
			echo "</li>\n";
		}


from BeautifulSoup import BeautifulSoup
import re
import urllib2

my_runs_url = "http://nikeplus.nike.com/nikeplus/v1/services/widget/get_public_run_list.jsp?userID=753216162"

page = urllib2.urlopen(my_runs_url)
soup = BeautifulSoup(page)