from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	context = {
		"leagues": League.objects.all(),

		# ############# SPORTS ORM I ###################
		# ******todas las ligas de béisbol*****
		# "leagues": League.objects.filter(sport="Baseball"),
		# ******todas las ligas de mujeres*****
		# "leagues": League.objects.filter(name__contains="Women"),
		# ******todas las ligas donde el deporte es cualquier tipo de hockey******
		# "leagues": League.objects.filter(sport__contains="hockey"),
		# ******todas las ligas donde el deporte no sea football******
		# "leagues": League.objects.exclude(sport="Football"),
		# ******todas las ligas que se llaman "conferencias"******
		# "leagues": League.objects.filter(name__contains="conference"),
		# ****** todas las ligas de la región atlántica*******
		# "leagues": League.objects.filter(name__contains="atlantic"),
		"teams": Team.objects.all(),
		# ******todos los equipos con sede en Dallas******
		# "teams": Team.objects.filter(location="Dallas"),
		# ******todos los equipos nombraron los Raptors******
		# "teams": Team.objects.filter(team_name_="Raptors"),
		# ******todos los equipos cuya ubicación incluye "Ciudad"******
		# "teams": Team.objects.filter(location__contains="city"),
		# ******todos los equipos cuyos nombres comienzan con "T"******
		# "teams": Team.objects.filter(team_name__startswith="T"),
		# ******todos los equipos, ordenados alfabéticamente por ubicación******
		# "teams": Team.objects.all().order_by("location")
		# ******todos los equipos, ordenados por nombre de equipo en orden alfabético inverso******
		# "teams": Team.objects.all().order_by("-team_name")
		"players": Player.objects.all(),
		# *****cada jugador con apellido "Cooper"*****
		# "players": Player.objects.filter(last_name="Cooper"),
		# *****cada jugador con nombre "Joshua"*****
		# "players": Player.objects.filter(first_name="Joshua"),
		# ***** todos los jugadores con el apellido "Cooper" EXCEPTO aquellos con "Joshua" como primer nombre*****
		# "players": Player.objects.filter(last_name="Cooper").exclude(first_name="Joshua")
		# *****todos los jugadores con nombre "Alexander" O nombre "Wyatt"*****
		# "players": Player.objects.filter(Q(first_name="Alexander") | Q(first_name="Wyatt"))

		# ############# SPORTS ORM II ###################
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")