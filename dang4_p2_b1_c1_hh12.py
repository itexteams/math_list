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


def bt_dang4_p2_b1_c1_hh12(self):
            # Khai báo biến
            a=randint(1,9)
            # Nội dung câu hỏi
            noidungcauhoi = '''Cho hình tứ diện đều $ABCD$ cạnh $%s$, $O$ là tâm của tam giác $BCD$, $M$ là trung điểm của $BC$. \n'''%(latex(a))

            # Các đáp án
            da_1_d = '\\True Ba vectơ $\\overrightarrow{AD}, \\overrightarrow{OM}$ và $\\overrightarrow{AO}$ đồng phẳng'
            da_1_s = 'Ba vectơ $\\overrightarrow{AD}, \\overrightarrow{OM}$ và $\\overrightarrow{AO}$ không đồng phẳng'
            list_da_1=[da_1_d,da_1_s]
            da_1=random.choice(list_da_1)

            da_2_d = '\\True $\\overrightarrow{BC}=2 \\overrightarrow{MC}$'
            da_2_s = '$\\overrightarrow{BC}=3 \\overrightarrow{MC}$'
            list_da_2=[da_2_d,da_2_s]
            da_2=random.choice(list_da_2)

            da_3_d = '\\True $\\overrightarrow{OD}=-2 \\overrightarrow{OM}$'
            da_3_s = '$\\overrightarrow{OD}=2 \\overrightarrow{OM}$'
            list_da_3=[da_3_d,da_3_s]
            da_3=random.choice(list_da_3)

            da_4_d = '\\True Độ dài vectơ $\\overrightarrow{AM}$ bằng $%s$'%(latex((a*sqrt(3))/2))
            da_4_s = 'Độ dài vectơ $\\overrightarrow{AM}$ bằng $%s$'%(latex((a*sqrt(3))))
            list_da_4=[da_4_d,da_4_s]
            da_4=random.choice(list_da_4)

            da_5_d = '\\True Góc giữa hai vectơ $\\overrightarrow{DA}$ và $\\overrightarrow{DB}$ bằng $60^\\circ$'
            da_5_s = 'Góc giữa hai vectơ $\\overrightarrow{DA}$ và $\\overrightarrow{DB}$ bằng $30^\\circ$'
            list_da_5=[da_5_d,da_5_s]
            da_5=random.choice(list_da_5)

            da_6_d = '\\True Góc giữa hai vectơ $\\overrightarrow{AB}$ và $\\overrightarrow{CA}$ bằng $120^\\circ$'
            da_6_s = 'Góc giữa hai vectơ $\\overrightarrow{AB}$ và $\\overrightarrow{CA}$ bằng $60^\\circ$'
            list_da_6=[da_6_d,da_6_s]
            da_6=random.choice(list_da_6)

            da_7_d = '\\True $\\overrightarrow{DC} \\cdot \\overrightarrow{DM} =%s$'%(latex(Rational(3*a**2,4)))
            da_7_s = '$\\overrightarrow{DC} \\cdot \\overrightarrow{DM} =%s$'%(latex(Rational(3*a**2,2)))
            list_da_7=[da_7_d,da_7_s]
            da_7=random.choice(list_da_7)

            da_8_d = '\\True $\\overrightarrow{AO}=\\dfrac{1}{3} \\overrightarrow{AD}+\\dfrac{2}{3} \\overrightarrow{AM}$'
            da_8_s = '$\\overrightarrow{AO}=\\dfrac{2}{3} \\overrightarrow{AD}+\\dfrac{2}{3} \\overrightarrow{AM}$'
            list_da_8=[da_8_d,da_8_s]
            da_8=random.choice(list_da_8)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_1 = [da_1, da_2, da_3, da_4, da_5, da_6, da_7, da_8]

            # Nội dung lời giải
            loigiai_1 = ('Ba đường thẳng $AD, OM$ và $AO$ cùng nằm trêm mặt phẳng $(ADM)$ nên ba vectơ $\\overrightarrow{AD}, \\overrightarrow{OM}$ và $\\overrightarrow{AO}$ đồng phẳng.'

                        )
            loigiai_2 = ('Vì $M$ là trung điểm của $BC$ nên ta có $\\overrightarrow{BC}=2 \\overrightarrow{MC}$.'
                        )
            loigiai_3 = ('$O$ là trong tâm của tam giác $BCD$ nên $OD=2OM$. \\\\ \n'
                        'Do đó $\\overrightarrow{OD}=-2 \\overrightarrow{OM}$.'
                        )
            loigiai_4 = ('$AM$ là đường trung tuyến của tam giác đều cạnh $%s$ nên $AM=%s$.\\\\ \n'
                        'Suy ra độ dài vectơ $\\overrightarrow{AM}$ bằng $%s$.'
                        %(latex(a),latex((a*sqrt(3))/2),latex((a*sqrt(3))/2)
                        ))
            loigiai_5 = ('Vì $ABD$ là tam giác đều nên góc giữa hai vectơ $\\overrightarrow{DA}$ và $\\overrightarrow{DB}$ bằng $60^\\circ$.'

                        )
            loigiai_6 = ('Ta có $\\left( \\overrightarrow{AB}, \\overrightarrow{CA} \\right)=180^\\circ-60^\\circ=120^\\circ$.'

                        )
            loigiai_7 = ('Ta có $\\overrightarrow{DC} \\cdot \\overrightarrow{DM} =\\left| \\overrightarrow{DC} \\right| \\cdot \\left| \\overrightarrow{DM} \\right| \\cos \\left( \\overrightarrow{DC}, \\overrightarrow{DM} \\right) =DM \\cdot DC \\cos 30^\\circ=%s \\cdot %s =%s$.'
                        %(latex(a),latex((a*sqrt(3))/2),latex(Rational(3*a**2,4))
                        ))

            loigiai_8 = ('Ta có \\\\ \n'
                        '$\\overrightarrow{AO}=\\overrightarrow{AD}+\\overrightarrow{DO}=\\overrightarrow{AD}+\\dfrac{2}{3}\\overrightarrow{DM}$ \\\\ \n'
                        '\\hspace*{1cm} $=\\overrightarrow{AD}+\\dfrac{2}{3} \\left( \\overrightarrow{DA}+\\overrightarrow{AM} \\right)$ \\\\ \n'
                        '\\hspace*{1cm} $=\\overrightarrow{AD}-\\dfrac{2}{3} \\overrightarrow{AD}++\\dfrac{2}{3} \\overrightarrow{AM}$ \\\\ \n'
                        '\\hspace*{1cm} $=\\dfrac{1}{3} \\overrightarrow{AD}+\\dfrac{2}{3} \\overrightarrow{AM}$.'
                        )

            # Đưa các lời giải vào danh sách lời giải
            list_2 = [loigiai_1, loigiai_2, loigiai_3, loigiai_4, loigiai_5, loigiai_6, loigiai_7, loigiai_8]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined = list(zip(list_1, list_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers, shuffled_solutions = zip(*combined)

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choiceTFn \n'
                '{'+str(shuffled_answers[0])+'}\n'
                '{'+str(shuffled_answers[1])+'}\n'
                '{'+str(shuffled_answers[2])+'}\n'
                '{'+str(shuffled_answers[3])+'}\n'
                '\\loigiai{ \n'

                    '\\begin{center} \n'
                    '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]  \n'
                    '\\clip(-0.8452379780986704,-2.560699168362529) rectangle (4.61490847740837,2.9530833034068493); \n'
                    '\\draw (0.,0.)-- (1.,-2.); \n'
                    '\\draw (1.,-2.)-- (4.,0.); \n'
                    '\\draw [dash pattern=on 2pt off 2pt] (0.,0.)-- (2.4962411645971265,-1.0025058902685822);  \n'
                    '\\draw [dash pattern=on 2pt off 2pt] (1.5646489020095042,-0.6283726759709743)-- (1.5576555504545262,2.2879967017537326); \n'
                    '\\draw (1.5576555504545262,2.2879967017537326)-- (0.,0.); \n'
                    '\\draw (1.5576555504545262,2.2879967017537326)-- (1.,-2.); \n'
                    '\\draw (1.5576555504545262,2.2879967017537326)-- (4.,0.); \n'
                    '\\draw [dash pattern=on 2pt off 2pt] (0.,0.)-- (4.,0.); \n'
                    '\\draw (1.5576555504545262,2.2879967017537326)-- (2.4962411645971265,-1.0025058902685822); \n'
                    '\\draw (1.364565891910073,2.8994472871445014) node[anchor=north west] {$A$}; \n'
                    '\\draw (0.7745697130242434,-1.927794176466822) node[anchor=north west] {$B$}; \n'
                    '\\draw (4.05709390827995,0.31419130329932593) node[anchor=north west] {$C$}; \n'
                    '\\draw (-0.6,0.33564570980426517) node[anchor=north west] {$D$}; \n'
                    '\\draw (2.544558249681732,-0.8550738512198612) node[anchor=north west] {$M$}; \n'
                    '\\draw (1.15,-0.5654393634031819) node[anchor=north west] {$O$}; \n'
                    '\\end{tikzpicture} \n'
                    '\\end{center} \n'

                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions[0])+'\n'
                '\\item '+str(shuffled_solutions[1])+'\n'
                '\\item '+str(shuffled_solutions[2])+'\n'
                '\\item '+str(shuffled_solutions[3])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac')
            return content

