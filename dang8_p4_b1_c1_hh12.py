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


def bt_dang8_p4_b1_c1_hh12(self):
            # Khai báo biến
            lisdang=['1','2','3','4']
            dang=random.choice(lisdang)
            if dang=='1':
                a=randint(4,15)


                # Nội dung câu hỏi
                noidungcauhoi = ('Cho hình chóp tứ giác đều $S.ABCD$ có tất cả các cạnh bằng $%s$.\\\\ \n'
                                'a) Vectơ nào bằng vectơ $\\vec{AB}$.\\\\ \n'
                                'b) Tính $\\vec{SA}\\cdot\\vec{SB}$. \\\\ \n'
                                'c) Chứng minh rằng $\\vec{SA}+\\vec{SC}=\\vec{SB}+\\vec{SD}.$'
                                %(latex(a)
                                ))

                # Nội dung lời giải
                loigiai = ('\\begin{center} \n' 
                            '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] \n'  
                                '\\clip(-0.809906902845595,-0.683575353673238) rectangle (5.188413574762594,4.605164625795179);\n' 
                                '\\draw (0.,0.)-- (3.,0.); \n'
                                '\\draw (3.,0.)-- (4.5,1.5); \n'
                                '\\draw [dash pattern=on 2pt off 2pt] (4.5,1.5)-- (1.5,1.5); \n'
                                '\\draw [dash pattern=on 2pt off 2pt] (1.5,1.5)-- (0.,0.); \n'
                                '\\draw [dash pattern=on 2pt off 2pt] (1.5,1.5)-- (3.,0.); \n'
                                '\\draw [dash pattern=on 2pt off 2pt] (0.,0.)-- (4.5,1.5); \n'
                                '\\draw [dash pattern=on 2pt off 2pt] (2.25,0.75)-- (2.283864069043802,4.009117007357772); \n'
                                '\\draw [dash pattern=on 2pt off 2pt] (2.283864069043802,4.009117007357772)-- (1.5,1.5); \n'
                                '\\draw (2.283864069043802,4.009117007357772)-- (0.,0.);\n' 
                                '\\draw (2.283864069043802,4.009117007357772)-- (4.5,1.5);\n' 
                                '\\draw (2.283864069043802,4.009117007357772)-- (3.,0.); \n'
                                '\\draw (2,4.55) node[anchor=north west] {$S$}; \n'
                                '\\draw (-0.5,0.18684339071154624) node[anchor=north west] {$A$}; \n'
                                '\\draw (2.9745224205665113,0.054388364392122565) node[anchor=north west] {$B$}; \n'
                                '\\draw (4.554521663091066,1.8236090730872816) node[anchor=north west] {$C$}; \n'
                                '\\draw (0.9,1.8898365862469935) node[anchor=north west] {$D$};\n' 
                                '\\draw (1.8,0.8112742290745436) node[anchor=north west] {$O$}; \n'
                            '\\end{tikzpicture} \n'
                        '\\end{center} \n'
                        '\\begin{enumEX}[a)]{1} \n'
                                '\\item  $\\vec{DC}=\\vec{AB}$'
                                '\\item Vì tam giác $SAB$ đều nên $(\\vec{SA},\\vec{SB})=60^{\\circ}.$\\\\ \n'
                                'Tích vô hướng của hai vectơ $\\vec{SA}$ và $\\vec{SB}$ là \\\\ \n'
                                '\\hspace*{1cm}$\\vec{SA}\\cdot\\vec{SB}=\\abs{\\vec{SA}}\\cdot\\abs{\\vec{SB}}\\cos(\\vec{SA},\\vec{SB})=%s\\cdot %s\\cos 60^{\\circ}=%s$.'
                                '\\item Gọi $O$ là giao điểm của $AC$ và $BD$, ta có \\\\ \n'
                                '$\\vec{SA}+\\vec{SC}=\\vec{SB}+\\vec{SD} \\Leftrightarrow \\vec{SA}+\\vec{SC}-(\\vec{SB}+\\vec{SD})=\\vec{0} \\Leftrightarrow 2\\vec{SO}-2\\vec{SO}=\\vec{0}$(luôn đúng).\\\\ \n'
                                'Vậy $\\vec{SA}+\\vec{SC}=\\vec{SB}+\\vec{SD}$.'
                                '\\end{enumEX}'

                        %(latex(a),latex(a),latex(nsimplify(a**2/2))
                        ))
            if dang=='2':
                a=randint(4,15)


                # Nội dung câu hỏi
                noidungcauhoi = ('Cho hình chóp tứ giác đều $S.ABCD$ có tất cả các cạnh bằng $%s$. Gọi $O$ là giao điểm của $AC$ và $BD$.\\\\ \n'
                                'a) Vectơ nào bằng vectơ $\\vec{AD}$.\\\\ \n'
                                'b) Tính $\\vec{SA}\\cdot\\vec{SD}$. \\\\ \n'
                                'c) Chứng minh rằng $\\vec{SA}+\\vec{SB}+\\vec{SC}+\\vec{SD}=4\\vec{SO}$.'
                                %(latex(a)
                                ))

                # Nội dung lời giải
                loigiai = ('\\begin{center} \n' 
                            '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] \n'  
                                '\\clip(-0.809906902845595,-0.683575353673238) rectangle (5.188413574762594,4.605164625795179);\n' 
                                '\\draw (0.,0.)-- (3.,0.); \n'
                                '\\draw (3.,0.)-- (4.5,1.5); \n'
                                '\\draw [dash pattern=on 2pt off 2pt] (4.5,1.5)-- (1.5,1.5); \n'
                                '\\draw [dash pattern=on 2pt off 2pt] (1.5,1.5)-- (0.,0.); \n'
                                '\\draw [dash pattern=on 2pt off 2pt] (1.5,1.5)-- (3.,0.); \n'
                                '\\draw [dash pattern=on 2pt off 2pt] (0.,0.)-- (4.5,1.5); \n'
                                '\\draw [dash pattern=on 2pt off 2pt] (2.25,0.75)-- (2.283864069043802,4.009117007357772); \n'
                                '\\draw [dash pattern=on 2pt off 2pt] (2.283864069043802,4.009117007357772)-- (1.5,1.5); \n'
                                '\\draw (2.283864069043802,4.009117007357772)-- (0.,0.);\n' 
                                '\\draw (2.283864069043802,4.009117007357772)-- (4.5,1.5);\n' 
                                '\\draw (2.283864069043802,4.009117007357772)-- (3.,0.); \n'
                                '\\draw (2,4.55) node[anchor=north west] {$S$}; \n'
                                '\\draw (-0.5,0.18684339071154624) node[anchor=north west] {$A$}; \n'
                                '\\draw (2.9745224205665113,0.054388364392122565) node[anchor=north west] {$B$}; \n'
                                '\\draw (4.554521663091066,1.8236090730872816) node[anchor=north west] {$C$}; \n'
                                '\\draw (0.9,1.8898365862469935) node[anchor=north west] {$D$};\n' 
                                '\\draw (1.8,0.8112742290745436) node[anchor=north west] {$O$}; \n'
                            '\\end{tikzpicture} \n'
                        '\\end{center} \n'
                        '\\begin{enumEX}[a)]{1} \n'
                                '\\item  $\\vec{BC}=\\vec{AD}$'
                                '\\item Vì tam giác $SAD$ đều nên $(\\vec{SA},\\vec{SD})=60^{\\circ}.$\\\\ \n'
                                'Tích vô hướng của hai vectơ $\\vec{SA}$ và $\\vec{SD}$ là \\\\ \n'
                                '\\hspace*{1cm}$\\vec{SA}\\cdot\\vec{SD}=\\abs{\\vec{SA}}\\cdot\\abs{\\vec{SD}}\\cos(\\vec{SA},\\vec{SD})=%s\\cdot %s\\cos 60^{\\circ}=%s$.'
                                '\\item Ta có \\\\ \n'
                                '$VT=\\vec{SA}+\\vec{SB}+\\vec{SC}+\\vec{SD}=(\\vec{SA}+\\vec{SC})+(\\vec{SB}+\\vec{SD})=2\\vec{SO}+2\\vec{SO}=4\\vec{SO}=VP$ (đpcm).\\\\ \n'
                                '\\end{enumEX}'

                        %(latex(a),latex(a),latex(nsimplify(a**2/2))
                        ))
            if dang=='3':
                a=randint(4,15)


                # Nội dung câu hỏi
                noidungcauhoi = ('Cho hình chóp tứ giác đều $S.ABCD$ có tất cả các cạnh bằng $%s$.\\\\ \n'
                                'a) Vectơ nào bằng vectơ $\\vec{DC}$.\\\\ \n'
                                'b) Tính $\\vec{SC}\\cdot\\vec{SD}$. \\\\ \n'
                                'c) Chứng minh rằng $\\vec{SA}-\\vec{SB}+\\vec{SC}-\\vec{SD}=\\vec{0}$.'
                                %(latex(a)
                                ))

                # Nội dung lời giải
                loigiai = ('\\begin{center} \n' 
                            '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] \n'  
                                '\\clip(-0.809906902845595,-0.683575353673238) rectangle (5.188413574762594,4.605164625795179);\n' 
                                '\\draw (0.,0.)-- (3.,0.); \n'
                                '\\draw (3.,0.)-- (4.5,1.5); \n'
                                '\\draw [dash pattern=on 2pt off 2pt] (4.5,1.5)-- (1.5,1.5); \n'
                                '\\draw [dash pattern=on 2pt off 2pt] (1.5,1.5)-- (0.,0.); \n'
                                '\\draw [dash pattern=on 2pt off 2pt] (1.5,1.5)-- (3.,0.); \n'
                                '\\draw [dash pattern=on 2pt off 2pt] (0.,0.)-- (4.5,1.5); \n'
                                '\\draw [dash pattern=on 2pt off 2pt] (2.25,0.75)-- (2.283864069043802,4.009117007357772); \n'
                                '\\draw [dash pattern=on 2pt off 2pt] (2.283864069043802,4.009117007357772)-- (1.5,1.5); \n'
                                '\\draw (2.283864069043802,4.009117007357772)-- (0.,0.);\n' 
                                '\\draw (2.283864069043802,4.009117007357772)-- (4.5,1.5);\n' 
                                '\\draw (2.283864069043802,4.009117007357772)-- (3.,0.); \n'
                                '\\draw (2,4.55) node[anchor=north west] {$S$}; \n'
                                '\\draw (-0.5,0.18684339071154624) node[anchor=north west] {$A$}; \n'
                                '\\draw (2.9745224205665113,0.054388364392122565) node[anchor=north west] {$B$}; \n'
                                '\\draw (4.554521663091066,1.8236090730872816) node[anchor=north west] {$C$}; \n'
                                '\\draw (0.9,1.8898365862469935) node[anchor=north west] {$D$};\n' 
                                '\\draw (1.8,0.8112742290745436) node[anchor=north west] {$O$}; \n'
                            '\\end{tikzpicture} \n'
                        '\\end{center} \n'
                        '\\begin{enumEX}[a)]{1} \n'
                                '\\item  $\\vec{AB}=\\vec{DC}$'
                                '\\item Vì tam giác $SCD$ đều nên $(\\vec{SC},\\vec{SD})=60^{\\circ}.$\\\\ \n'
                                'Tích vô hướng của hai vectơ $\\vec{SC}$ và $\\vec{SD}$ là \\\\ \n'
                                '\\hspace*{1cm}$\\vec{SC}\\cdot\\vec{SD}=\\abs{\\vec{SC}}\\cdot\\abs{\\vec{SD}}\\cos(\\vec{SC},\\vec{SD})=%s\\cdot %s\\cos 60^{\\circ}=%s$.'
                                '\\item Ta có \\\\ \n'
                                '$VT=\\vec{SA}-\\vec{SB}+\\vec{SC}-\\vec{SD}=(\\vec{SA}-\\vec{SB})+(\\vec{SC}-\\vec{SD})=\\vec{BA}+\\vec{DC}=\\vec{0}=VP$ (đpcm).\\\\ \n'
                                '(vì $\\vec{BA}$ và  $\\vec{DC}$ là hai vectơ đối).'
                                '\\end{enumEX}'

                        %(latex(a),latex(a),latex(nsimplify(a**2/2))
                        ))
            if dang=='4':
                a=randint(4,15)


                # Nội dung câu hỏi
                noidungcauhoi = ('Cho hình chóp tứ giác đều $S.ABCD$ có tất cả các cạnh bằng $%s$. Gọi $O$ là giao điểm của $AC$ và $BD$, $I$ là trung điểm của $SO$\\\\ \n'
                                'a) Vectơ nào bằng vectơ $\\vec{CB}$.\\\\ \n'
                                'b) Tính $\\vec{SB}\\cdot\\vec{SC}$. \\\\ \n'
                                'c) Chứng minh rằng $\\vec{SA}+\\vec{SB}+\\vec{SC}+\\vec{SD}=8\\vec{SI}$.'
                                %(latex(a)
                                ))

                # Nội dung lời giải
                loigiai = ('\\begin{center} \n' 
                            '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] \n'  
                                '\\clip(-0.809906902845595,-0.683575353673238) rectangle (5.188413574762594,4.605164625795179);\n' 
                                '\\draw (0.,0.)-- (3.,0.); \n'
                                '\\draw (3.,0.)-- (4.5,1.5); \n'
                                '\\draw [dash pattern=on 2pt off 2pt] (4.5,1.5)-- (1.5,1.5); \n'
                                '\\draw [dash pattern=on 2pt off 2pt] (1.5,1.5)-- (0.,0.); \n'
                                '\\draw [dash pattern=on 2pt off 2pt] (1.5,1.5)-- (3.,0.); \n'
                                '\\draw [dash pattern=on 2pt off 2pt] (0.,0.)-- (4.5,1.5); \n'
                                '\\draw [dash pattern=on 2pt off 2pt] (2.25,0.75)-- (2.283864069043802,4.009117007357772); \n'
                                '\\draw [dash pattern=on 2pt off 2pt] (2.283864069043802,4.009117007357772)-- (1.5,1.5); \n'
                                '\\draw (2.283864069043802,4.009117007357772)-- (0.,0.);\n' 
                                '\\draw (2.283864069043802,4.009117007357772)-- (4.5,1.5);\n' 
                                '\\draw (2.283864069043802,4.009117007357772)-- (3.,0.); \n'
                                '\\draw (2,4.55) node[anchor=north west] {$S$}; \n'
                                '\\draw (-0.5,0.18684339071154624) node[anchor=north west] {$A$}; \n'
                                '\\draw (2.9745224205665113,0.054388364392122565) node[anchor=north west] {$B$}; \n'
                                '\\draw (4.554521663091066,1.8236090730872816) node[anchor=north west] {$C$}; \n'
                                '\\draw (0.9,1.8898365862469935) node[anchor=north west] {$D$};\n' 
                                '\\draw (1.8,0.8112742290745436) node[anchor=north west] {$O$}; \n'
                            '\\end{tikzpicture} \n'
                        '\\end{center} \n'
                        '\\begin{enumEX}[a)]{1} \n'
                                '\\item  $\\vec{CB}=\\vec{DA}$'
                                '\\item Vì tam giác $SBC$ đều nên $(\\vec{SB},\\vec{SC})=60^{\\circ}.$\\\\ \n'
                                'Tích vô hướng của hai vectơ $\\vec{SB}$ và $\\vec{SC}$ là \\\\ \n'
                                '\\hspace*{1cm}$\\vec{SB}\\cdot\\vec{SC}=\\abs{\\vec{SB}}\\cdot\\abs{\\vec{SC}}\\cos(\\vec{SB},\\vec{SC})=%s\\cdot %s\\cos 60^{\\circ}=%s$.'
                                '\\item Ta có \\\\ \n'
                                '$VT=\\vec{SA}+\\vec{SB}+\\vec{SC}+\\vec{SD}=(\\vec{SA}+\\vec{SC})+(\\vec{SB}+\\vec{SD})=4\\vec{SO}=8\\vec{SI}=VP$ (đpcm).\\\\ \n'
                                '\\end{enumEX}'

                        %(latex(a),latex(a),latex(nsimplify(a**2/2))
                        ))



            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content

