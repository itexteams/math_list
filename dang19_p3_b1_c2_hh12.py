import sys
from PyQt5.QtWidgets import QApplication, QColorDialog, QMainWindow, QSplitter, QTreeWidget, QSpacerItem, QSizePolicy, QTreeWidgetItem, QCheckBox, QFileDialog, QVBoxLayout, QTextEdit, QPushButton, QWidget, QLabel, QLineEdit, QDialog, QAction, QMessageBox, QScrollBar, QHeaderView, QMenu, QGridLayout
from sympy import *
from sympy.abc import x
import sympy as sp
from sympy import symbols,sqrt,evaluate,Subs,latex, Rational, expand, simplify, integrate
import random
import math
from sympy import Rational
from fractions import Fraction as frac
from random import randint
from PyQt5.QtGui import QTextCursor
from PyQt5.QtGui import QFont
import hashlib
import uuid
import os
from sympy import symbols, Eq, solve
import numpy as np
from PyQt5.QtGui import QIcon
from math import factorial
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextDocument
from subprocess import run, CalledProcessError
import shutil
from PyQt5.QtWidgets import QProgressBar
from docx import Document
from PyQt5 import QtGui
import re
import pandas as pd
from PyQt5.QtGui import QPixmap
import subprocess
import platform
import json
from decimal import Decimal, ROUND_HALF_UP
from PyQt5.QtWidgets import QComboBox, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSpinBox, QTreeWidget, QTreeWidgetItem, QCheckBox, QTextEdit, QPushButton, QHBoxLayout
from random import randint, choice, shuffle
from sympy import latex
from fractions import Fraction
from collections import Counter
from random import sample
import shutil
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import qrcode
import json
import glob
import os
import platform
import subprocess
import hashlib
import base64
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox)
from sympy import symbols, solve, Lt
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
import re
import pyperclip
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

import google.generativeai as genai
from sympy.abc import x, y, z, t
import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox
)
from pdf2image import convert_from_path
from math import degrees
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font
from openpyxl.utils import get_column_letter
from sympy import simplify, collect
from itertools import combinations
import itertools
from PyQt5.QtCore import QSettings
import sys
import os
import platform
import subprocess
import hashlib
import time
from datetime import datetime, timedelta
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
)
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPropertyAnimation, pyqtProperty
from functools import wraps
import re
import uuid
import json, base64
from datetime import datetime
from nacl.signing import VerifyKey
from nacl.encoding import HexEncoder
from nacl.exceptions import BadSignatureError
### CÔNG CỤ
import sys
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QDialog, 
    QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, 
    QLabel, QSlider, QDoubleSpinBox, QGroupBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D


def bt_dang19_p3_b1_c2_hh12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Các bộ số Pythagore để đảm bảo tọa độ nguyên
                triples = [(3, 4, 5), (4, 3, 5), (6, 8, 10), (8, 6, 10), (5, 12, 13), (12, 5, 13), (9, 12, 15), (12, 9, 15)]
                m, n, k = random.choice(triples)

                # Kết quả S = a + b + c + d
                # Mặt phẳng có pt dạng nx - my = 0 -> a=n, b=-m, c=0, d=0
                kq = n - m

                # Các đáp án trắc nghiệm
                du = ['$%s$'%(kq)]
                da = random.choice(du)

                # Tạo các phương án sai (đảm bảo không trùng với đáp án đúng)
                s_raw = [kq + 1, kq - 1, m + n, m - n, kq + 2, kq - 2, -kq]
                s_unique = []
                for val in s_raw:
                    if val != kq and val not in s_unique:
                        s_unique.append(val)

                random.shuffle(s_unique)

                das1 = '$%s$'%(s_unique[0])
                das2 = '$%s$'%(s_unique[1])
                das3 = '$%s$'%(s_unique[2])
                hinhve=r'''\begin{tikzpicture}[scale=1,line width=0.2,line join=round, line cap=round, >=stealth, declare function={r=0.15; gocA=95; gocB=68;}]
            		\definecolor{brightmaroon}{rgb}{0.76, 0.13, 0.28}
            		\definecolor{sealbrown}{rgb}{0.2, 0.08, 0.08}
            		\definecolor{cobalt}{rgb}{0.0, 0.28, 0.67}
            		\definecolor{apricot}{rgb}{0.98, 0.81, 0.69}
            		\path 
            		(0.5,0) coordinate (O)
            		+(-10:5) coordinate (M)
            		(5.5,0) coordinate (H)
            		;
            		\draw[->,thick] (O)--+(-110:1) node[right]{$x$};
            		\draw[->,thick] (O)--+(0:6.5) node[below]{$y$};
            		\draw[->,thick] (O)--+(90:3) node[left]{$z$};
            		\fill (O) circle (1pt) node[shift=(-60:0.3)]{$O$}
            		(M) circle (1pt);
            		\draw[dashed,blue] (O)--(M)node[midway,below]{$5$\,m}--(H)node[midway,right]{$3$\,m};
            		\pic[draw,angle eccentricity=2,angle radius=1.5mm]{right angle=M--H--O};
            		\draw [blue] (1.58,2.43) .. controls +(12.9:1.34) and +(108.0:2.19) .. (M);
            		\tikzset{Vball/.pic={
            				\clip (0,0) circle (r);
            				\foreach \ang/\colA/\colB/\colC in {90/yellow/blue/white, 210/white/yellow/blue, 330/blue/white/yellow}{
            					\begin{scope}[rotate=\ang]
            						\path (0,0) to[bend right=15] coordinate[pos=0.35] (P1) coordinate[pos=0.68] (P2) (0:r);
            						\fill[\colA] (0,0) to[bend right=15] (0:r) arc(0:120:r) to[bend left=15] (0,0);
            						\fill[\colB] (P1) to[bend right=22] (gocA:r) arc(gocA:0:r) to[bend left=15] (P1);
            						\fill[\colC] (P2) to[bend right=18] (gocB:r) arc(gocB:0:r) to[bend left=15] (P2);
            					\end{scope}
            				}
            				\foreach \ang in {90, 210, 330}{
            					\begin{scope}[rotate=\ang]
            						\draw (0,0) to[bend right=15] coordinate[pos=0.35] (P1) coordinate[pos=0.68] (P2) (0:r)
            						(P1) to[bend right=22] (gocA:r)
            						(P2) to[bend right=18] (gocB:r);
            					\end{scope}
            				}
            				\draw (0,0) circle (r);
            		}}
            		\pic at (1.6,2.4) {Vball};
            		\draw [fill=apricot] (0.84,2.04)
            		.. controls +(-31.8:0.06) and +(157.7:0.07) .. (0.92,1.95)
            		.. controls +(-110.6:0.07) and +(63.4:0.06) .. (0.915,1.85)
            		.. controls +(-88.3:0.04) and +(-6.5:0.06) .. (0.73,1.79)
            		.. controls +(3.8:0.01) and +(-70.2:0.05) .. (0.75,1.86)
            		.. controls +(131.8:0.05) and +(135:0.07) .. (0.79,1.91)
            		.. controls +(79.4:0.07) and +(-167.6:0.06)
            		.. cycle;
            		\draw (0.88,1.89) 
            		.. controls +(10:0.02) and +(-122:0.01) .. (0.91,1.90)
            		(0.865,1.99) .. controls +(145.3:0.02) and +(94.8:0.02) .. (0.84,1.96);
            		\filldraw (0.86,1.97)
            		.. controls +(45:0.01) and +(58:0.01) .. 
            		(0.87,1.96)
            		.. controls +(-111.8:0.01) and +(-116.6:0.01) .. cycle;
            		\draw [fill=sealbrown!90] (0.74,1.79)
            		.. controls +(3.8:0.01) and +(-70.2:0.05) .. (0.75,1.86)
            		.. controls +(131.8:0.05) and +(135:0.07) .. (0.79,1.91)
            		.. controls +(54.1:0.08) and +(-167.6:0.06) .. (0.845,2.045)
            		.. controls +(128.9:0.08) and +(81.8:0.16) .. (0.61,1.94)
            		.. controls +(-178.3:0.08) and +(118:0.15) .. (0.50,1.71)
            		.. controls +(-42.6:0.09) and +(155.9:0.12) .. (0.59,1.51)
            		.. controls +(100.2:0.12) and +(-53.5:0.14) .. (0.65,1.74)
            		.. controls +(129.2:0.08) and +(-152.2:0.07) .. (0.62,1.90)
            		.. controls +(-86.6:0.06) and +(172.9:0.06) .. cycle
            		;
            		\draw[fill=cobalt] (0.93,1.24)
            		.. controls +(-105.4:0.18) and +(3.6:0.14) ..(0.55,0.58)
            		.. controls +(-150.2:0.16) and +(46.9:0.18) .. (0.24,0.31)
            		.. controls +(162.9:0.05) and +(-90:0.06) .. (0.15,0.42)
            		.. controls +(61.5:0.16) and +(-137.6:0.18) .. (0.48,0.76)
            		.. controls +(49:0.29) and +(-140.6:0.35) .. (0.70,1.31)
            		.. controls +(10.4:0.06) and +(141.7:0.08) ..
            		(0.93,1.24)
            		.. controls +(-96.8:0.24) and  +(72:0.15) .. (0.80,0.75)
            		.. controls +(-118.5:0.22) and  +(83.4:0.30) .. (0.62,0.18)
            		.. controls +(-176.4:0.06) and +(-45:0.05) .. (0.47,0.23)
            		.. controls +(89.1:0.11)  and +(-104.9:0.11).. (0.53,0.56)
            		;
            		\draw [fill=apricot!90] (0.97,1.71)
            		.. controls +(37.9:0.21) and +(-117.1:0.18) .. (1.27,2.12)
            		.. controls +(17.1:0.03) and +(-122.5:0.03) .. (1.33,2.18)
            		.. controls +(40.8:0.03) and +(-54.0:0.01) .. (1.37,2.22)
            		.. controls +(123.7:0.01) and +(27.2:0.04) .. (1.32,2.20)
            		.. controls +(45.0:0.04) and +(-72.6:0.02) .. (1.36,2.26)
            		.. controls +(149.0:0.01) and +(40.3:0.06) .. (1.29,2.21)
            		.. controls +(51.8:0.06) and +(-90.0:0.02) .. (1.35,2.29)
            		.. controls +(137.1:0.02) and +(57.1:0.03) .. (1.29,2.24)
            		;
            		\draw [fill=apricot!90] (0.93,1.88)
            		.. controls +(45.0:0.12) and +(-119.6:0.06) .. (1.17,2.17)
            		.. controls +(64.8:0.04) and +(-151.9:0.02) .. (1.18,2.31)
            		.. controls +(0.0:0.01) and +(80.5:0.02) .. (1.19,2.26)
            		.. controls +(71.9:0.11) and +(-139.1:0.02) .. (1.23,2.37)
            		.. controls +(-5.4:0.02) and +(85.8:0.03) .. (1.22,2.28)
            		.. controls +(55.0:0.02) and +(161.6:0.01) .. (1.28,2.37)
            		.. controls +(-31.6:0.02) and +(59.9:0.04) .. (1.24,2.27)
            		.. controls +(52.3:0.04) and +(135.0:0.01) .. (1.31,2.35)
            		.. controls +(-24.4:0.02) and +(49.3:0.05) .. (1.26,2.26)
            		.. controls +(42.3:0.04) and +(140.7:0.01) .. (1.33,2.31)
            		.. controls +(-49.8:0.02) and +(58.7:0.03) .. (1.28,2.24)
            		.. controls +(-103.1:0.04) and +(55.0:0.04) .. (1.22,2.14)
            		.. controls +(-116.6:0.10) and +(49.3:0.24) .. (0.97,1.71)
            		;
            		\draw [white,thin] (0.79,1.293)
            		.. controls +(-108.4:0.21) and +(47.6:0.13) .. (0.56,0.74)
            		.. controls +(-129.2:0.14) and +(48.9:0.23) .. (0.16,0.378)
            		(0.81,1.29)
            		.. controls +(-108.4:0.21) and +(47.6:0.13) .. (0.57,0.72)
            		.. controls +(-129.2:0.14) and +(48.9:0.23) .. (0.17,0.36)
            		;
            		\draw[fill=white] (0.15,0.44)
            		.. controls +(-98:0.05) and +(167.2:0.05) .. (0.23,0.32)
            		.. controls +(-128.1:0.08) and +(91.4:0.04) .. (0.17,0.14)
            		.. controls +(-91.8:0.06) and +(-80.2:0.08) .. (0.08,0.16)
            		.. controls +(101.8:0.07) and +(-87.3:0.09) .. (0.07,0.41)
            		.. controls +(85.7:0.04) and +(176.5:0.03) .. cycle
            		(0.47,0.23)
            		.. controls +(-45:0.05) and +(-176.4:0.06) .. (0.62,0.18)
            		.. controls +(-86.6:0.05) and +(135.6:0.07) .. (0.65,0.03)
            		.. controls +(-42.9:0.06) and +(-34:0.06) .. (0.59,-0.03)
            		.. controls +(134.5:0.08) and +(-55.3:0.08) .. (0.43,0.15)
            		.. controls +(121.4:0.04) and +(-158.7:0.06) .. (0.47,0.23)
            		;
            		\draw [fill=brightmaroon] (0.69,1.32)
            		.. controls +(108:0.07) and +(-84:0.28) .. (0.69,1.65)
            		.. controls +(77.5:0.04) and +(-153.4:0.03) .. (0.72,1.76)
            		.. controls +(52.6:0.06) and +(-141:0.17) .. (0.94,1.89)
            		.. controls +(-94.6:0.08) and +(142.5:0.06) .. (0.99,1.72)
            		.. controls +(-104.9:0.02) and +(56.3:0.01) .. (0.96,1.68)
            		.. controls +(-32.7:0.08) and +(73.8:0.38) .. (0.93,1.24)
            		.. controls +(141.7:0.08) and +(10.4:0.06) .. cycle
            		(0.96,1.68)	
            		.. controls +(-133.6:0.04) and +(-5.2:0.03) .. (0.86,1.62)
            		;
            		\draw [fill=cobalt] (5.52,0.18)
            		.. controls +(123.9:0.09) and +(-96.6:0.06) .. (5.38,0.51)
            		.. controls +(61.9:0.11) and +(-148.3:0.08) .. (5.58,0.72)
            		.. controls +(-24.9:0.05) and +(-167.8:0.07) .. (5.74,0.69)
            		.. controls +(-116.2:0.16) and +(39.3:0.09) .. (5.55,0.44)
            		.. controls +(-78.4:0.1) and +(118.7:0.08) .. (5.65,0.19)
            		.. controls +(-132.3:0.03) and +(-19.8:0.06) .. cycle
            		(5.82,0.12)
            		.. controls +(124.3:0.13) and +(-115.2:0.05) .. (5.66,0.47)
            		.. controls +(92.3:0.07) and +(-110.3:0.08) .. (5.73,0.69)
            		.. controls +(5.7:0.08) and +(152.6:0.08) .. (5.94,0.66)
            		.. controls +(-125.4:0.1) and +(100.3:0.06) .. (5.82,0.44)
            		.. controls +(-67.1:0.08) and +(104:0.05) .. (5.93,0.15)
            		.. controls +(-123.7:0.03) and +(-10:0.05) .. cycle;
            		\draw [white,thin] (5.88,0.68)
            		.. controls +(-125:0.25) and +(119.3:0.32) .. (5.89,0.12)
            		(5.9,0.68)
            		.. controls +(-125:0.25) and +(119.3:0.32) .. (5.91,0.13);
            		\draw [fill=gray!80] (5.66,0.18)
            		.. controls +(-69.4:0.02) and +(70:0.03) .. (5.67,0.11)
            		.. controls +(-167.2:0.05) and +(-1.7:0.08) .. (5.42,0.1)
            		.. controls +(151.6:0.07) and +(-166:0.07) .. (5.51,0.18)
            		.. controls +(-36:0.03) and +(-164.1:0.05) .. cycle
            		(5.82,0.13)
            		.. controls +(-103.2:0.04) and +(122.7:0.04) .. (5.79,0.05)
            		.. controls +(-23.2:0.05) and +(-149.9:0.05) .. (5.95,0.06)
            		.. controls +(59.7:0.03) and +(-48.4:0.03) .. (5.94,0.14)--cycle;
            		\draw [fill=sealbrown!90] (5.71,1.23)
            		.. controls +(180:0.03) and +(22.1:0.09) .. (5.67,1.3)
            		.. controls +(108.4:0.03) and +(-39.3:0.03) .. (5.62,1.38)
            		.. controls +(180:0.03) and +(0:0.03) .. 
            		(5.52,1.38)
            		.. controls +(75.1:0.07) and +(136.5:0.06) .. (5.73,1.42)
            		.. controls +(-41.4:0.05) and +(57.5:0.12) .. (5.73,1.25)--cycle
            		;
            		\draw[fill=apricot] (5.71,1.23)
            		.. controls +(180:0.03) and +(22.1:0.09) .. (5.67,1.3)
            		.. controls +(108.4:0.03) and +(-39.3:0.03) .. (5.62,1.38)
            		.. controls +(180:0.03) and +(0:0.03) .. 
            		(5.53,1.38)
            		.. controls +(-95.3:0.05) and +(110:0.08) .. 
            		(5.54,1.22)
            		.. controls +(-21.8:0.05) and +(127.4:0.01).. (5.57,1.21) -- (5.57,1.2) -- (5.61,1.15)-- (5.7,1.21) --cycle
            		; 
            		\filldraw (5.6,1.32) ellipse (0.006 and 0.01)
            		(5.54,1.33) ellipse (0.005 and 0.01);
            		\draw (5.59,1.34)
            		.. controls +(79.2:0.01) and +(103:0.01) .. (5.62,1.33)
            		(5.53,1.35)
            		.. controls +(79.2:0.01) and +(103:0.01) .. (5.56,1.34)
            		(5.56,1.31)	.. controls +(-153.4:0.02) and +(-179.4:0.01) .. (5.55,1.28)
            		(5.54,1.26) .. controls +(-79.2:0.01) and +(-103:0.01) .. (5.58,1.26)
            		(5.78,1.01) -- (5.68,0.94)
            		.. controls +(114.2:0.06) and +(-30.3:0.04) .. (5.60,1.04)
            		.. controls +(58.1:0.04) and +(-147.3:0.05) .. (5.68,1.13)
            		;
            		\draw [fill=brightmaroon] (5.58,0.72)
            		.. controls +(36.3:0.05) and +(-61.2:0.06) .. (5.58,0.89)
            		.. controls +(129.1:0.05) and +(-41.8:0.10) .. (5.45,1.05)
            		.. controls +(57.4:0.08) and +(-156.4:0.05) .. (5.58,1.19)	-- (5.61,1.15)	-- (5.70,1.21)
            		.. controls +(0.0:0.12) and +(102.2:0.13) .. (5.91,0.89)
            		.. controls +(-62.0:0.09) and +(65.2:0.07) .. (5.94,0.66)
            		.. controls +(147.1:0.15) and +(-39.5:0.13) .. cycle
            		;
            		\draw [fill=apricot] (5.55,0.97)
            		.. controls +(-129.8:0.08) and +(-41.2:0.02) .. (5.12,0.8)
            		.. controls +(125.5:0.02) and +(-163.3:0.06) .. (5.2,0.84)
            		.. controls +(24.5:0.11) and +(-134.4:0.14) .. (5.46,1.05) -- cycle;
            		\draw [fill=apricot] (5.68,0.94)
            		.. controls +(-138.7:0.13) and +(15.6:0.21) .. (5.32,0.8)
            		.. controls +(-149:0.05) and +(-66.8:0.02) .. (5.2,0.7)
            		.. controls +(138.4:0.01) and +(-126.4:0.03) .. (5.24,0.76)
            		.. controls +(-137.6:0.03) and +(-32:0.01) .. (5.17,0.71)
            		.. controls +(118.6:0.01) and +(-137.1:0.04) .. (5.23,0.78)
            		.. controls +(-164.5:0.02) and +(-63.4:0.02) .. (5.14,0.73)
            		.. controls +(110.6:0.01) and +(-146.3:0.05) .. (5.22,0.8)
            		.. controls +(-159.4:0.03) and +(-38.7:0.01) .. (5.12,0.77)
            		.. controls +(119.7:0.02) and +(-154.4:0.03) .. (5.21,0.82)
            		.. controls +(28:0.04) and +(-93.8:0.02) .. (5.17,0.86)
            		.. controls +(82.6:0.02) and +(-173.3:0.04) .. (5.31,0.85)
            		.. controls +(24.2:0.2) and +(-120.7:0.1) .. (5.6,1.04)
            		.. controls +(-30.3:0.04) and +(114.2:0.06) ..	cycle	;
            	\end{tikzpicture}'''
                # Câu hỏi
                noidungcauhoi = (r'''\immini{Hai học sinh đang chuyền bóng. Bạn nữ ném bóng cho bạn nam. Quả bóng bay trên không, lệch sang phải và rơi xuống tại vị trí cách bạn nam $%s$ m, cách bạn nữ $%s$ m. Cho biết quỹ đạo của quả bóng nằm trong mặt phẳng $\left( P \right)$ vuông góc với mặt đất. Tổng $S = a+b+c+d$ bằng bao nhiêu với $a,b,c,d$ là các hệ số của phương trình mặt phẳng $\left( P \right)$ trong không gian $Oxyz$ (được mô tả trong hình vẽ) có dạng $ax+by+cz+d=0$ (với $a, b, c, d$ là các số nguyên tối giản và $a>0$)?}{%s}'''
                                 % (m, k, hinhve))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Mặt phẳng $\\left( Oxy \\right)$ có một vectơ pháp tuyến là $\\vec{n} = \\left( 0;0;1 \\right)$.\\\\
                         Do $\\left( P \\right) \\perp \\left( Oxy \\right)$, mà vectơ pháp tuyến $\\vec{n}$ của $\\left( Oxy \\right)$ có giá vuông góc với $\\left( Oxy \\right)$, nên giá của $\\vec{n}$ song song hoặc nằm trên $\\left( P \\right)$. Như vậy $\\vec{n}$ là một vectơ chỉ phương của $\\left( P \\right)$.\\\\
                         Mặt khác, theo hình vẽ, gọi $A$ là điểm rơi của quả bóng trên mặt đất. Dễ dàng thấy được $z_A = 0$ và $x_A = %s$. Trên mặt phẳng $\\left( Oxy \\right)$, ta có $OA = %s$ và $y_A > 0$. Như vậy tung độ của $A$ là $y_A = \\sqrt{%s^2 - %s^2} = %s$. Vậy ta có $A \\left( %s; %s; 0 \\right)$.\\\\
                         Theo hình vẽ, $\\left( P \\right)$ đi qua điểm $O \\left( 0;0;0 \\right)$ và $A \\left( %s; %s; 0 \\right)$, nên $\\vec{OA} = \\left( %s; %s; 0 \\right)$ là một vectơ chỉ phương khác của $\\left( P \\right)$. Ta dễ thấy rằng $\\vec{n} = \\left( 0;0;1 \\right)$ và $\\vec{OA} = \\left( %s; %s; 0 \\right)$ là hai vectơ không cùng phương, do đó $\\vec{n}$ và $\\vec{OA}$ là một cặp vectơ chỉ phương của $\\left( P \\right)$.\\\\
                         Như vậy một vectơ pháp tuyến của $\\left( P \\right)$ là:\\\\
                         $\\vec{n}_{\\left( P \\right)} = \\left[ \\vec{n}, \\vec{OA} \\right] = \\left( 0 \\cdot 0 - 1 \\cdot %s; 1 \\cdot %s - 0 \\cdot 0; 0 \\cdot %s - 0 \\cdot %s \\right) = \\left( -%s; %s; 0 \\right)$.\\\\
                         Vậy phương trình mặt phẳng $\\left( P \\right)$ đi qua $O \\left( 0;0;0 \\right)$ và có một vectơ pháp tuyến $\\vec{n}_{\\left( P \\right)} = \\left( -%s; %s; 0 \\right)$ là\\\\
                         $-%s \\left( x - 0 \\right) + %s \\left( y - 0 \\right) + 0 \\left( z - 0 \\right) = 0 \\Leftrightarrow -%sx + %sy = 0 \\Leftrightarrow %sx - %sy = 0$.\\\\
                         Từ đó ta có $a = %s$, $b = -%s$, $c = 0$, $d = 0$ (thoả mãn điều kiện hệ số nguyên tối giản và $a>0$).\\\\
                         Tổng $S = a+b+c+d = %s + \\left( -%s \\right) + 0 + 0 = %s$.'''
                         % (m, k, k, m, n, m, n,
                            m, n, m, n,
                            m, n,
                            n, m, n, m, n, m,
                            n, m,
                            n, m,
                            n, m, n, m,
                            n, m,
                            n, m, kq))

                dapan='\\shortans[0]{$%s$}\n'%(kq)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

