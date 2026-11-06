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


def bt_dang8_p3_b5_c2_hh11(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                a=randint(2,9)
                h1=Rational(5*a,2)  
                number = Decimal(float(h1))  # Số cần làm tròn
                kq = number.quantize(Decimal('1'), rounding=ROUND_HALF_UP)
                # Câu hỏi
                noidungcauhoi = ('''Cho tứ diện $ABCD$ có $AC = %s, BD = %s$. Gọi $M, N$ lần lượt là trung điểm $AD$ và $BC$. Biết $AC$ vuông góc $BD$. Độ dài cạnh $MN$ bằng bao nhiêu? (làm tròn kết quả đến hàng đơn vị).'''
                                %(latex(3*a),latex(4*a)
                                ))
                # Nội dung lời giải
                loigiai=('''\\begin{center}
                \\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]
                    \\clip(-1.0112795185093602,-2.7906691357274243) rectangle (4.660253258462629,3.9663244598037903);
                    \\draw [line width=1.pt ,dash pattern=on 2pt off 2pt] (0.,0.)-- (4.,0.);
                    \\draw [line width=1.pt ] (0.,0.)-- (1.,-2.);
                    \\draw [line width=1.pt ] (1.,-2.)-- (4.,0.);
                    \\draw [line width=1.pt ] (0.,0.)-- (2.,3.);
                    \\draw [line width=1.pt ] (2.,3.)-- (1.,-2.);
                    \\draw [line width=1.pt ] (2.,3.)-- (4.,0.);
                    \\draw [line width=1.pt ] (1.,1.5)-- (0.5,-1.);
                    \\draw [line width=1.pt ,dash pattern=on 2pt off 2pt] (0.5,-1.)-- (2.5,-1.);
                    \\draw [line width=1.pt ,dash pattern=on 2pt off 2pt] (2.5,-1.)-- (1.,1.5);
                    \\draw (-0.6,0.39787201879031764) node[anchor=north west] {$A$};
                    \\draw (0.8068673525773541,-1.9087322206480488) node[anchor=north west] {$B$};
                    \\draw (4.090386328719032,0.3571672380943465) node[anchor=north west] {$C$};
                    \\draw (1.8244868699766343,3.708527515395973) node[anchor=north west] {$D$};
                    \\draw (0.42695606608162273,2.1617458489490686) node[anchor=north west] {$M$};
                    \\draw (-0.1,-0.8775444430167791) node[anchor=north west] {$P$};
                    \\draw (2.5978777032000875,-0.8775444430167791) node[anchor=north west] {$N$};
                \\end{tikzpicture}
            \\end{center}
                        Gọi $P$ là trung điểm $AB$. \\\\
                        Ta có $\\begin{cases} AC // PN \\\\ BD // PM \\end{cases} \\Rightarrow PN \\perp PM$ và $PN = \\frac{AC}{2} = %s; PM = \\frac{BD}{2} = %s$. \\\\
                        $MN = \\sqrt{PM^2 + PN^2} = %s$.'''
                        %(latex(Rational(3*a,2)),latex(2*a),latex(Rational(5*a,2))
                        ))
            #Đáp án
            dapan=' \\shortans[0]{$%s$} '%(latex(kq))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

