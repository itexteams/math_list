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


def bt_dang6_p3_b5_c2_hh11(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                a=randint(5,19)
                h1=a*sqrt(2)
                number = Decimal(float(h1))  # Số cần làm tròn
                kq = number.quantize(Decimal('1'), rounding=ROUND_HALF_UP)
                # Câu hỏi
                noidungcauhoi = ('''Cho tứ diện $ABCD$ có tam giác $ABD$ đều cạnh bằng $%s$, tam giác $ABC$ vuông tại $B, BC = %s \\sqrt{3}$. Biết khoảng cách giữa hai đường thẳng chéo nhau $AB$ và $CD$ bằng $%s$. Độ dài cạnh $CD$ bằng bao nhiêu? (làm tròn kết quả đến hàng đơn vị).'''
                                %(latex(2*a),latex(a),latex(a*sqrt(11)/2)
                                ))

                # Nội dung lời giải
                loigiai=('''\\begin{center}
                \\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]
                        \\clip(-0.7399143138695521,-0.8504079225527974) rectangle (6.858311416045074,5.038217018131031);
                        \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (0.,0.)-- (2.,1.);
                        \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (2.,1.)-- (6.,1.);
                        \\draw [line width=1.pt] (6.,1.)-- (4.,0.);
                        \\draw [line width=1.pt] (4.,0.)-- (0.,0.);
                        \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (2.,4.)-- (2.,1.);
                        \\draw [line width=1.pt] (2.,4.)-- (0.,0.);
                        \\draw [line width=1.pt] (2.,4.)-- (4.,0.);
                        \\draw [line width=1.pt] (2.,4.)-- (6.,1.);
                        \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (2.,4.)-- (1.0217348532898571,0.5108674266449286);
                        \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (1.0217348532898571,0.5108674266449286)-- (4.985853139390019,0.4929265696950096);
                        \\draw [line width=1.pt] (4.985853139390019,0.4929265696950096)-- (2.,4.);
                        \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (1.0217348532898571,0.5108674266449286)-- (3.1800653814448365,2.6139385455061666);
                        \\draw (2.0687155541524618,1.6597202203654244) node[anchor=north west] {$A$};
                        \\draw (-0.44141258876576317,0.16721159484648174) node[anchor=north west] {$B$};
                        \\draw (4.049681548023061,0.12650681415051057) node[anchor=north west] {$C$};
                        \\draw (1.8244868699766343,4.671873991867291) node[anchor=north west] {$D$};
                        \\draw (6.0984888430536115,1.6461519601334342) node[anchor=north west] {$E$};
                        \\draw (1.0782325572171623,0.6556689631981357) node[anchor=north west] {$M$};
                        \\draw (5.080869325654332,0.628532442734155) node[anchor=north west] {$N$};
                        \\draw (3.2,2.9) node[anchor=north west] {$H$};
                \\end{tikzpicture}
            \\end{center}
                        Dựng hình chữ nhật $ABCE$, gọi $M, N$ lần lượt là trung điểm $AB, CE$, $MH \\perp DN$ tại $H$.\\\\
                        Ta có \\\\
                        $\\begin{cases} AB \\perp DM \\\\ AB \\perp MN \\end{cases} \\Rightarrow AB \\perp (DMN) \\Rightarrow CE \\perp (DMN) \\Rightarrow MH \\perp CE$.\\\\
                        $\\begin{cases} MH \\perp DN \\\\ MH \\perp CE \\end{cases} \\Rightarrow MH \\perp (CDE)$ tại $H \\Rightarrow d(AB,CD) = d[M;(CDE)] = MH = %s$.\\\\
                        Tam giác $DMN$ có $DM = MN = %s\\sqrt{3} \\Rightarrow H$ là trung điểm $DN$. \\\\
                        Mà $HN = \\sqrt{MN^2 - MH^2} = %s$ $\\Rightarrow DN = %s$.\\\\
                        Xét tam giác $DNC$ vuông tại $N$ nên $CD = \\sqrt{DN^2 + CN^2} = %s \\sqrt{2}$.'''
                        %(latex(a*sqrt(11)/2),latex(a),latex(Rational(a,2)),
                        latex(a),latex(a)
                        ))

            #Đáp án
            dapan=' \\shortans[0]{$%s$} '%(latex(kq))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

