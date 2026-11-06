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


def bt_dang5_p4_b1_c2_hh11(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                ab=randint(2,9)
                sa=randint(2,9)
                while ab==sa:
                    ab=randint(2,9)
                    sa=randint(2,9)
                gtri=Rational(sa,ab)
                goc1=atan(gtri)
                gocz=goc1*180/pi

                h1=gocz
                number = Decimal(float(h1))  # Số cần làm tròn
                goc = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('''                     
                                Cho hình chóp $SzzABCD$ có đáy là hình thang vuông tại $A$ và $D$, $AB=%sa$, $SA$ vuông góc với $AB$ và $AD$, $SA=%s a$zz Tính góc giữa hai đường thẳng $CD$ và $SB$zz
                                '''
                                %(latex(ab),latex(sa)
                                ))

                # Nội dung lời giải
                loigiai=('''\\begin{center}
                \\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1zz0cm,y=1zz0cm]
                    \\clip(-3zz037360728023805,-2zz793146952698919) rectangle (6zz802529049776581,4zz015638690209989);
                    \\draw [line width=1zzpt,dash pattern=on 2pt off 2pt] (0zz,0zz)-- (-2zz,-2zz);
                    \\draw [line width=1zzpt] (-2zz,-2zz)-- (1zz,-2zz);
                    \\draw [line width=1zzpt] (1zz,-2zz)-- (6zz,0zz);
                    \\draw [line width=1zzpt,dash pattern=on 2pt off 2pt] (0zz,0zz)-- (6zz,0zz);
                    \\draw [line width=1zzpt,dash pattern=on 2pt off 2pt] (0zz,0zz)-- (0zz,3zz);
                    \\draw [line width=1zzpt] (0zz,3zz)-- (-2zz,-2zz);
                    \\draw [line width=1zzpt] (0zz,3zz)-- (1zz,-2zz);
                    \\draw [line width=1zzpt] (0zz,3zz)-- (6zz,0zz);
                    \\draw (-0zz23022980507012897,3zz7618023833471566) node[anchor=north west] {$S$};
                    \\draw (-0zz66,0zz5216565839804177) node[anchor=north west] {$A$};
                    \\draw (-2zz6,-1zz7778017252475906) node[anchor=north west] {$B$};
                    \\draw (1,-2) node[anchor=north west] {$C$};
                    \\draw (6zz055951676650603,0zz38727265681774187) node[anchor=north west] {$D$};
                \\end{tikzpicture}
            \\end{center}             
                    Do $DC//AB$ $\\Rightarrow \\left(DC,AB\\right)=\\left(AB,SB\\right)=\\alpha$zz \\\\
                    Tam giác $SAB$ vuông tại $A$ nên $\\alpha$ là góc nhọn, khi đó $\\tan \\alpha=\\dfrac{SA}{AB}=%s$ suy ra $\\alpha=%s^\\circ$zz\\\\
                    Vậy góc giữa hai đường thẳng $DC$ và $SB$ bằng $%s^\\circ$zz'''
                        %(latex(Rational(sa,ab)),latex(goc),latex(goc)
                        ))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('.', ',').replace('zz', '.')
            return content   

