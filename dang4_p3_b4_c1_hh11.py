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


def bt_dang4_p3_b4_c1_hh11(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # Random tỷ số AB/BC = m/n sao cho m < n hoặc m != n
        pairs = [(2, 3), (3, 4), (1, 3), (2, 5), (3, 5), (4, 5), (1, 2), (5, 6), (3, 7)]
        m, n = random.choice(pairs)

        # Tính giá trị thập phân và làm tròn đến hàng phần trăm
        val = Decimal(m) / Decimal(n)
        kq = val.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        kq_str = str(kq).replace('.', ',')

        # Hình vẽ TikZ 3 mặt phẳng song song và 2 cát tuyến
        hinhve ='''\\begin{center}
        	\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
        		\\draw  [line width=1]  (136,44.6) -- (302,44.6) -- (257,74) -- (91,74) -- cycle ;
        		\\draw  [line width=1]  (128,118.6) -- (294,118.6) -- (249,148) -- (83,148) -- cycle ;
        		\\draw  [line width=1]  (123,194.6) -- (289,194.6) -- (244,224) -- (78,224) -- cycle ;
        		\\draw [line width=1]    (164,20.6) -- (156.67,59.33) ;
        		\\draw [line width=1]    (222,19.6) -- (223.73,55.47) ;
        		\\draw [line width=1]    (156.67,59.33) -- (223.73,55.47) ;
        		\\draw [line width=1]    (144.4,126.13) -- (229.07,127.47) ;
        		\\draw [line width=1]    (144.4,126.13) -- (198.4,138.8) ;
        		\\draw [line width=1]    (198.4,138.8) -- (229.07,127.47) ;
        		\\draw [line width=1]    (129.33,204) -- (233.73,211.47) ;
        		\\draw [line width=1]    (153.73,74.8) -- (144.4,126.13) ;
        		\\draw [line width=1]    (139.73,148.8) -- (129.33,204) ;
        		\\draw [line width=1]    (125.33,224.6) -- (118,263.33) ;
        		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (156.67,59.33) -- (153.73,74.8) ;
        		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (144.4,126.13) -- (139.73,148.8) ;
        		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (129.33,204) -- (125.33,224.6) ;
        		\\draw [line width=1]    (225.07,74.8) -- (229.07,127.47) ;
        		\\draw [line width=1]    (230.4,146.8) -- (233.73,211.47) ;
        		\\draw [line width=1]    (234.67,224.93) -- (236.4,260.8) ;
        		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (223.73,55.47) -- (225.07,74.8) ;
        		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (229.07,127.47) -- (230.4,146.8) ;
        		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (233.73,211.47) -- (234.67,224.93) ;
        		\\draw [line width=1]    (165.07,74.13) -- (198.4,138.8) ;
        		\\draw [line width=1]    (202.4,148.13) -- (233.73,211.47) ;
        		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (156.67,59.33) -- (165.07,74.13) ;
        		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (198.4,138.8) -- (202.4,148.13) ;
        		\\draw (104,62) node [anchor=north west][inner sep=0.75pt]  [font=\\scriptsize]  {$P)$};
        		\\draw (98.67,134) node [anchor=north west][inner sep=0.75pt]  [font=\\scriptsize]  {$Q)$};
        		\\draw (92,210) node [anchor=north west][inner sep=0.75pt]  [font=\\scriptsize]  {$R)$};
        		\\draw (146,11.33) node [anchor=north west][inner sep=0.75pt]  [font=\\footnotesize]  {$d$};
        		\\draw (206,10) node [anchor=north west][inner sep=0.75pt]  [font=\\footnotesize]  {$d'$};
        		\\draw (136,46) node [anchor=north west][inner sep=0.75pt]    {$A$};
        		\\draw (125.33,119) node [anchor=north west][inner sep=0.75pt]    {$B$};
        		\\draw (111.33,199) node [anchor=north west][inner sep=0.75pt]    {$C$};
        		\\draw (225.33,46) node [anchor=north west][inner sep=0.75pt]    {$A'$};
        		\\draw (230.67,119.93) node [anchor=north west][inner sep=0.75pt]    {$B'$};
        		\\draw (234.67,194.6) node [anchor=north west][inner sep=0.75pt]    {$C'$};
        		\\draw (184,146.6) node [anchor=north west][inner sep=0.75pt]    {$D$};		
        	\\end{tikzpicture}
        \\end{center}'''


        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho $3$ mặt phẳng $(P),(Q),(R)$ đôi một song song với nhau. Đường thẳng $a$ cắt các mặt phẳng $(P),(Q),(R)$ lần lượt tại $A,B,C$ sao cho $\\frac{AB}{BC} = \\frac{%d}{%d}$ và đường thẳng $b$ cắt các mặt phẳng $(P),(Q),(R)$ lần lượt tại $A',B',C'$. Tỉ số $\\frac{A'B'}{B'C'}$ bằng bao nhiêu? (kết quả làm tròn đến hàng phần trăm).'''
                         % (m, n)
                         )

        # Nội dung lời giải
        loigiai = (hinhve+'''Theo định lí Thales trong không gian, ta có: $\\frac{AB}{BC} = \\frac{A'B'}{B'C'} = \\frac{%d}{%d} \\approx %s$.\\\\
    Vậy tỉ số $\\frac{A'B'}{B'C'} \\approx %s$.'''
                   % (m, n, kq_str, kq_str)
                   )

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = (
        '\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan) +
        '\\loigiai{ \n' + str(loigiai) + '}\n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content

