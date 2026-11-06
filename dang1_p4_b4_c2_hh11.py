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


def bt_dang1_p4_b4_c2_hh11(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                a=randint(2,9)
                b=randint(2,9)
                kq=Rational(2*b,a)

                # Câu hỏi
                noidungcauhoi = ('''Cho hình chóp tứ giác đều $S.ABCD$ có cạnh đáy bằng $%s$ và chiều cao bằng $%s$. Tính tang của góc giữa mặt bên và mặt đáy.'''
                                %(latex(a),latex(b)
                                ))
                # Nội dung lời giải
                loigiai=('''\\begin{center}
                \\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]
                    \\clip(-0.8213223140495864,-0.8276033057851219) rectangle (6.980330578512394,4.990578512396689);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (0.,0.)-- (2.,1.);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (2.,1.)-- (6.,1.);
                    \\draw [line width=1.pt] (6.,1.)-- (4.,0.);
                    \\draw [line width=1.pt] (4.,0.)-- (0.,0.);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (2.,1.)-- (4.,0.);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (0.,0.)-- (6.,1.);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (2.9467107438016518,0.5266446280991741)-- (3.,4.);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (3.,4.)-- (2.,1.);
                    \\draw [line width=1.pt] (3.,4.)-- (0.,0.);
                    \\draw [line width=1.pt] (3.,4.)-- (6.,1.);
                    \\draw [line width=1.pt] (3.,4.)-- (4.,0.);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (3.,4.)-- (1.0350413223140496,0.5175206611570248);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (1.0350413223140496,0.5175206611570248)-- (2.9467107438016518,0.5266446280991741);
                    \\draw [shift={(1.1599063635457607,0.6210380626975429)},line width=1.pt]  plot[domain=-0.19277739318664722:1.1676840544427483,variable=\\t]({1.*0.5243872285167787*cos(\\t r)+0.*0.5243872285167787*sin(\\t r)},{0.*0.5243872285167787*cos(\\t r)+1.*0.5243872285167787*sin(\\t r)});
                    \\draw (2.7654545454545443,4.6) node[anchor=north west] {$S$};
                    \\draw (-0.5568595041322312,0.24677685950413297) node[anchor=north west] {$A$};
                    \\draw (4.021652892561982,0.2137190082644636) node[anchor=north west] {$B$};
                    \\draw (6.104297520661155,1.4864462809917347) node[anchor=north west] {$C$};
                    \\draw (2.1373553719008256,1.7178512396694203) node[anchor=north west] {$D$};
                    \\draw (2.5836363636363626,0.5) node[anchor=north west] {$O$};
                    \\draw (0.5340495867768593,1.1228099173553716) node[anchor=north west] {$M$};
                \\end{tikzpicture}
            \\end{center}
            Gọi $M$ là trung điểm của $AD$ và $O$ là tâm của đáy. \\\\
            Góc giữa mặt bên và mặt đáy bằng $\\widehat{SMO}$, với $OM=%s$. \\\\
            Xét tam giác $SOM$ vuông tại $O$, ta có $\\tan \\widehat{SMO}=\\frac{SO}{OM}=\\frac{%s}{%s}=%s$.'''
                        %(latex(Rational(a,2)),
                        latex(b),latex(Rational(a,2)),latex(kq)
                        ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

