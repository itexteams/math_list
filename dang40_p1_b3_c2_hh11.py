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


def bt_dang40_p1_b3_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random góc tạo bởi cạnh bên và đáy (30, 45, 60 độ)
                # Để đảm bảo tính toán đẹp và giống mẫu, ta chọn các góc đặc biệt
                list_goc = [30, 45, 60]
                goc_dung = random.choice(list_goc)

                # Tính toán khoảng cách d = AK dựa trên góc
                # AH = a*sqrt(3)/2 (độ dài đường cao tam giác đều cạnh a)
                # Trong tam giác vuông A'AH, AK là đường cao hạ từ A xuống AA'
                # sin(A'AH) = AK / AH => AK = AH * sin(A'AH)

                if goc_dung == 30:
                    khoang_cach_tex = "\\frac{a\\sqrt{3}}{4}"
                    sin_val_tex = "\\frac{1}{2}"
                elif goc_dung == 45:
                    khoang_cach_tex = "\\frac{a\\sqrt{6}}{4}"
                    sin_val_tex = "\\frac{\\sqrt{2}}{2}"
                else: # 60 độ
                    khoang_cach_tex = "\\frac{3a}{4}"
                    sin_val_tex = "\\frac{\\sqrt{3}}{2}"

                # Các đáp án trắc nghiệm
                du = ["$%s^\\circ$" % goc_dung]
                da = random.choice(du)

                s = ["$30^\\circ$", "$45^\\circ$", "$60^\\circ$", "$90^\\circ$"]
                if da in s:
                    s.remove(da)

                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ("Cho hình lăng trụ $ABC.A'B'C'$, đáy $ABC$ là tam giác vuông tại $B$, $AB=a$, $\\widehat{ACB}=30^\\circ$. $M$ là trung điểm $AC$. Hình chiếu vuông góc của đỉnh $A'$ lên mặt phẳng $(ABC)$ là trung điểm $H$ của $BM$. Khoảng cách từ $C'$ đến mặt phẳng $(BMB')$ bằng $%s$. Góc tạo bởi cạnh bên và mặt phẳng đáy của hình lăng trụ là"
                                 % khoang_cach_tex)

                # Các đáp án
                da_d = ("\\True " + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                loigiai = ("Vì $CC' // BB'$ nên $CC' // (BMB')$, suy ra $d\\left(C', (BMB')\\right) = d\\left(C, (BMB')\\right)$.\\\\ "
                           "Mặt khác, $M$ là trung điểm của $AC$ và $M \\in BM \\subset (BMB')$ nên $d\\left(C, (BMB')\\right) = d\\left(A, (BMB')\\right)$.\\\\ "
                           "Theo giả thiết, $d\\left(A, (BMB')\\right) = %s$.\\\\ "
                           "Trong tam giác vuông $ABC$ có $AC = \\frac{AB}{\\sin 30^\\circ} = 2a$. \\\\ "
                           "Vì $M$ là trung điểm cạnh huyền $AC$ nên $BM = AM = \\frac{1}{2}AC = a$. \\\\ "
                           "Xét tam giác $ABM$ có $AB=a, AM=a, BM=a$ nên tam giác $ABM$ là tam giác đều cạnh $a$. \\\\ "
                           "Vì $H$ là trung điểm của $BM$ nên $AH \\perp BM$ và $AH = \\frac{a\\sqrt{3}}{2}$. \\\\ "
                           "Dựng hình bình hành $AA'H'H$ suy ra $HH' // AA'$. Vì $A'H \\perp (ABC)$ nên $AA'$ là cạnh bên, góc giữa cạnh bên và đáy là $\\widehat{A'AH}$.\\\\ "
                           "Ta có $\\begin{cases} BM \\perp AH \\\\ BM \\perp A'H \\end{cases} \\Rightarrow BM \\perp (AA'H'H)$.\\\\ "
                           "Kẻ $AK \\perp HH'$ tại $K$. Vì $BM \\perp (AA'H'H)$ nên $BM \\perp AK$. \\\\ "
                           "Từ đó $AK \\perp (BMB')$ nên $d\\left(A, (BMB')\\right) = AK = %s$. \\\\ "
                           "Trong hình bình hành $AA'H'H$, do $HH' // AA'$ nên $AK$ cũng là đường cao hạ từ $A$ xuống $AA'$ trong tam giác vuông $A'AH$. \\\\ "
                           "Trong tam giác vuông $A'AH$, ta có $\\sin \\widehat{A'AH} = \\frac{AK}{AH} = \\frac{%s}{\\frac{a\\sqrt{3}}{2}} = %s$. \\\\ "
                           "Vậy $\\widehat{A'AH} = %s^\\circ$."
                           % (khoang_cach_tex, khoang_cach_tex, khoang_cach_tex, sin_val_tex, goc_dung))

                # Hình vẽ TikZ
                hinh_ve = (r'''\begin{center}
            	\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            		\draw [line width=1]    (106.47,46.4) -- (226.47,46.4) ;
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (86.47,166.4) -- (206.47,166.4) ;
            		\draw [line width=1]    (106.47,46.4) -- (126.47,86.4) ;
            		\draw [line width=1]    (86.47,166.4) -- (106.47,206.4) ;
            		\draw [line width=1]    (86.47,166.4) -- (106.47,46.4) ;
            		\draw [line width=1]    (106.47,206.4) -- (126.47,86.4) ;
            		\draw [line width=1]    (206.47,166.4) -- (226.47,46.4) ;
            		\draw [line width=1]    (126.47,86.4) -- (226.47,46.4) ;
            		\draw [line width=1]    (106.47,206.4) -- (206.47,166.4) ; 
            		\draw [line width=1]    (126.47,86.4) -- (166.47,46.4) ;
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (106.47,206.4) -- (146.47,166.4) ;
            		\draw [line width=1]    (146.47,66.4) -- (106.47,46.4) ;
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (126.47,186.4) -- (86.47,166.4) ;
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (126.47,186.4) -- (146.47,66.4) ;
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (126.47,186.4) -- (106.47,46.4) ;
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (146.47,166.4) -- (126.47,86.4) ;
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (129.47,174.4) -- (86.47,166.4) ;
            		\draw (67,150) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$A$};
            		\draw (97,206) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$B$};
            		\draw (210,158) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$C$};
            		\draw (83,32) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$A'$};
            		\draw (109,78) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$B'$};
            		\draw (227,34) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$C'$};
            		\draw (146,147) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$M$};
            		\draw (126.47,186.4) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$H$};
            		\draw (134,45) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$H'$};
            		\draw (133,169) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$K$};
            	\end{tikzpicture}
            \end{center}'''
                    )

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n' 
                       '\\choice \n'
                       '{' + str(list_1[0]) + '}\n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '\\loigiai{' + hinh_ve+ str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

