from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Q, Count

from . import team_maker
import leagues

def index(request):
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),

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
		# *****cada jugador con apellido "Cooper"*****
		# "players": Player.objects.filter(last_name="Cooper"),
		# *****cada jugador con nombre "Joshua"*****
		# "players": Player.objects.filter(first_name="Joshua"),
		# ***** todos los jugadores con el apellido "Cooper" EXCEPTO aquellos con "Joshua" como primer nombre*****
		# "players": Player.objects.filter(last_name="Cooper").exclude(first_name="Joshua")
		# *****todos los jugadores con nombre "Alexander" O nombre "Wyatt"*****
		# "players": Player.objects.filter(Q(first_name="Alexander") | Q(first_name="Wyatt"))

		# ############# SPORTS ORM II ###################
		# ****** todos los equipos en la Atlantic Soccer Conference******
		# "teams": Team.objects.filter(league="5"),
		# ******todos los jugadores (actuales) en los Boston Penguins*****
		# "players": Player.objects.filter(curr_team="28"),
		# ****** todos los jugadores (actuales) en la International Collegiate Baseball Conference*****
		# "players": Player.objects.filter(curr_team__league_id=7, last_name="Lopez")
		# ****** todos los jugadores de fútbol******
		# "players": Player.objects.filter(curr_team__league__sport="Soccer"),
		# ******  todos los equipos con un jugador (actual) llamado "Sophia"******
		# "teams": Team.objects.filter(curr_players__first_name="Sophia"),
		# ******todas las ligas con un jugador (actual) llamado "Sophia"******
		# "leagues" : League.objects.filter(teams__curr_players__first_name="Sophia")
		# ****** todos con el apellido "Flores" que NO (actualmente) juegan para los Washington Roughriders******
		# "players": Player.objects.filter(all_teams__curr_players__first_name="Sophia"),
		# ******todos con el apellido "Flores" que NO (actualmente) juegan para los Washington Roughriders******
		# "players": Player.objects.filter(last_name="Flores").exclude(curr_team_id=10),
		# ******todos los equipos, pasados y presentes, con los que Samuel Evans ha jugado******
		# "teams": Team.objects.filter(all_players__first_name="Samuel", all_players__last_name="Evans"),
		# ******todos los jugadores, pasados y presentes, con los gatos tigre de Manitoba******
		# "players": Player.objects.filter(all_teams=37),
		# ******todos los jugadores que anteriormente estaban (pero que no lo están) con los Wichita Vikings******
		# "players": Player.objects.filter(all_teams=40).exclude(curr_team="40"),
		# ******cada equipo para el que Jacob Gray jugó antes de unirse a los Oregon Colts******
		# "teams": Team.objects.exclude(team_name="Colts").filter(all_players__first_name="Jacob",all_players__last_name="Gray"),
		# *****todos llamados "Joshua" que alguna vez han jugado en la Federación Atlántica de Jugadores de Béisbol Amateur*****
		# "players": Player.objects.filter(first_name="Joshua").filter(all_teams__league="3"),
		# ******todos los equipos que han tenido 12 o más jugadores, pasados y presentes.******
		# "teams": Team.objects.annotate(todos_jugadores=Count('all_players')).filter(todos_jugadores__gt=11),
		# ******todos los jugadores y el número de equipos para los que jugó, ordenados por la cantidad de equipos para los que han jugado******
		# "players": Player.objects.all().annotate(equipos=Count('all_teams')).order_by('-equipos')




	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")