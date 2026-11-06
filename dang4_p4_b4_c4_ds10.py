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


def bt_dang4_p4_b4_c4_ds10(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                x=symbols('x')
                k=randint(1,9)
                ab=2*k
                bc=13*k
                cd=8*k
                da=5*k
                bt=expand((x+ab)**2+(sqrt(da**2-x**2)+cd)**2, x)
                bt1=2*cd*sqrt(da**2-x**2)
                bt2=bc**2-2*ab*x-ab**2-da**2-cd**2

                bt3=bt1**2 
                bt4=bt2**2

                bt5=expand(bt3-bt4, x)

                equation = Eq(bt5, 0)
                solutions = solve(equation, x)
                x1, x2 = solutions[0], solutions[1]

                hb=x2+ab
                hc=sqrt(da**2-x2**2)+cd
                hbc=Rational(hb*hc,2)

                had=Rational(x2*sqrt(da**2-x2**2),2)


                # Nội dung câu hỏi
                noidungcauhoi = ('\\immini{'
                                'Cho tứ giác $ABCD$ có $AB \\bot CD, AB=%s, BC=%s, CD=%s, DA=%s$ như hình vẽ. Gọi $H$ là giao điểm của $AB$ và $CD$ và đặt $x=AH$. Tính diện tích tứ giác $ABCD$. \n'
                                '}{' 
                                '''
                                \\definecolor{ffqqqq}{rgb}{1.,0.,0.}
                                \\scalebox{0.7}{ 
                                \\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] 
                                        \\clip(-0.6843632062151567,-0.6182544876693714) rectangle (8.262714663891067,4.206708949712756);
                                        \\draw [line width=1.pt ,color=ffqqqq] (0.,0.)-- (0.,1.5);
                                        \\draw [line width=1.pt ,dashed] (0.,1.5)-- (0.,3.5);
                                        \\draw [line width=1.pt ,dashed] (0.,3.5)-- (3.,3.5);
                                        \\draw [line width=1.pt ,color=ffqqqq] (3.,3.5)-- (7.5,3.5);
                                        \\draw [line width=1.pt ,color=ffqqqq] (0.,1.5)-- (3.,3.5);
                                        \\draw [line width=1.pt ,color=ffqqqq] (0.,0.)-- (7.5,3.5);
                                        \\draw (-0.6,1.727741514364852) node[anchor=north west] {$A$};
                                        \\draw (-0.5,0.046602678899032) node[anchor=north west] {$B$};
                                        \\draw (7.6548452544571,3.7887987307269024) node[anchor=north west] {$C$};
                                        \\draw (2.9723512099110607,4.0262477187870465) node[anchor=north west] {$D$};
                                        \\draw (-0.5,3.978757921175018) node[anchor=north west] {$H$};
                                        \\draw (-0.5,2.962476252277601) node[anchor=north west] {$x$};
                                        \\draw (-0.5,1.0723823073188543) node[anchor=north west] {$%s$};
                                        \\draw (1.1392450220867492,2.962476252277601) node[anchor=north west] {$%s$};
                                        \\draw (4.985918628661081,4.045243637831859) node[anchor=north west] {$%s$};
                                        \\draw (3.551726740777812,1.6707537572304174) node[anchor=north west] {$%s$};
                                \\end{tikzpicture}}
                                '''
                                '}'
                                %(latex(ab),latex(bc),latex(cd),latex(da),
                                latex(ab),latex(da),latex(cd),latex(bc)
                                ))

                # Nội dung lời giải
                loigiai = ('Trong tam giác vuông $AHD$, ta có \\\\ \n'
                        '\\hspace*{1cm} $HD^2=AD^2-AH^2 =%s-x^2$ nên $HD=\\sqrt{%s-x^2}$. \\\\ \n'
                        'Suy ra \\\\ \n'
                        '\\hspace*{1cm} $HB=x+%s$ và $HC=\\sqrt{%s-x^2}+%s$. \\\\ \n'
                        'Xét tam giác $BHC$, ta có \\\\ \n'
                        '\\hspace*{1cm} $HB^2+HC^2=BC^2 \\Leftrightarrow (x+%s)^2+\\left( \\sqrt{%s-x^2}+%s \\right)^2=%s$ \\\\ \n'
                        '\\hspace*{4.75cm} $\\Leftrightarrow %s=%s$ \\\\ \n'
                        '\\hspace*{4.75cm} $\\Leftrightarrow %s=%s$ \\\\ \n'
                        '\\hspace*{4.75cm} $\\Leftrightarrow %s=%s$ \\\\ \n'
                        '\\hspace*{4.75cm} $\\Leftrightarrow %s=0$ \\\\ \n'
                        '\\hspace*{4.75cm} $\\Leftrightarrow x=%s$ (loại) hoặc $x=%s$. \\\\ \n'
                        'Suy ra $HB=%s$ và $HC=%s$. \\\\ \n'
                        'Diện tích tam giác $HBC$ là $S_1=\\dfrac{1}{2}HB \\cdot HC =\\dfrac{1}{2} \\cdot %s \\cdot %s=%s$.\\\\ \n'
                        'Diện tích tam giác $HAD$ là $S_2=\\dfrac{1}{2}HA \\cdot HD =\\dfrac{1}{2} \\cdot %s \\cdot %s=%s$.\\\\ \n'
                        'Vậy diện tích tứ giác $ABCD$ là $S=S_1-S_2=%s-%s=%s$.'

                        %(latex(da**2),latex(da**2),
                            latex(ab),latex(da**2),latex(cd),
                            latex(ab), latex(da**2),latex(cd),latex(bc**2),
                            latex(bt),latex(bc**2),
                            latex(bt1),latex(bt2),
                            latex(bt3),latex(bt4),
                            latex(bt5),latex(x1),latex(x2),
                            latex(x2+ab),latex(sqrt(da**2-x2**2)+cd),
                            latex(hb),latex(hc),latex(hbc),
                            latex(x2),latex(sqrt(da**2-x2**2)),latex(had),
                            latex(hbc),latex(had),latex(hbc-had)
                        ))


            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content

