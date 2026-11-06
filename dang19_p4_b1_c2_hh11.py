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


def bt_dang19_p4_b1_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến ký hiệu
            a = symbols('a')

            # Bước 3: Suy nghĩ tìm cách random bài toán
            # Random hệ số k cho cạnh của hình chóp (cạnh bằng k*a)
            k = random.choice([1, 2, 3, 4, 5])
            canh = k * a
            canh_sq = (k**2)

            # Tính toán giá trị đúng: MS.CB = (ka)^2 / 2
            # Lời giải chi tiết dựa trên: MS.CB = 1/2 OC^2 + 1/2 OD^2
            # Với OC = OD = (ka * sqrt(2)) / 2 => OC^2 = (k^2 * a^2) / 2
            kq_val = Rational(canh_sq, 2)
            da_dung = kq_val * a**2

            # Bước 4: Điều chỉnh các phương án sai
            s1 = -Rational(canh_sq, 2) * a**2
            s2 = Rational(canh_sq, 3) * a**2
            s3 = (sqrt(2) * Rational(canh_sq, 2)) * a**2
            s4 = Rational(canh_sq, 4) * a**2

            list_wrong = [s1, s2, s3, s4]
            random.shuffle(list_wrong)

            # Chọn 3 đáp án sai không trùng đáp án đúng
            final_wrong = []
            for sw in list_wrong:
                if sw != da_dung and len(final_wrong) < 3:
                    final_wrong.append(sw)

            das1, das2, das3 = final_wrong

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có tất cả các cạnh bên và cạnh đáy đều bằng $%s$ và $ABCD$ là hình vuông. Gọi $M$ là trung điểm của $CD$. Tính $\\vec{MS} \\cdot \\vec{CB}$.
            \\begin{center}
            \\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            	\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (80.47,130.07) -- (212.47,131.07) ;
            	\\draw [line width=1]    (33.47,171.07) -- (165.47,172.07) ;
            	\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (33.47,171.07) -- (80.47,130.07) ;
            	\\draw [line width=1]    (165.47,172.07) -- (212.47,131.07) ;
            	\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (80.47,130.07) -- (165.47,172.07) ;
            	\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (33.47,171.07) -- (212.47,131.07) ;
            	\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (122.97,151.07) -- (188.97,151.57) ;
            	\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (122.97,151.07) -- (121.47,41.07) ;
            	\\draw [line width=1]    (121.47,41.07) -- (33.47,171.07) ;
            	\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (121.47,41.07) -- (80.47,130.07) ;
            	\\draw [line width=1]    (121.47,41.07) -- (165.47,172.07) ;
            	\\draw [line width=1]    (121.47,41.07) -- (212.47,131.07) ;
            	\\draw (114,17) node [anchor=north west][inner sep=0.75pt]    {$S$};
            	\\draw (65,114) node [anchor=north west][inner sep=0.75pt]    {$A$};
            	\\draw (16,167) node [anchor=north west][inner sep=0.75pt]    {$B$};
            	\\draw (160,175) node [anchor=north west][inner sep=0.75pt]    {$C$};
            	\\draw (215,118) node [anchor=north west][inner sep=0.75pt]    {$D$};
            	\\draw (110,152) node [anchor=north west][inner sep=0.75pt]    {$O$};
            	\\draw (192,145) node [anchor=north west][inner sep=0.75pt]    {$M$};
            \\end{tikzpicture}
            \\end{center}''' % (latex(canh)))

            # Các đáp án
            da_d = ('\\True $%s$' % (latex(da_dung)))
            da_s1 = ('$%s$' % (latex(das1)))
            da_s2 = ('$%s$' % (latex(das2)))
            da_s3 = ('$%s$' % (latex(das3)))

            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Nội dung lời giải chi tiết
            # OC^2 = ( (ka*sqrt(2))/2 )^2 = k^2*a^2 / 2
            oc_sq_latex = latex(Rational(canh_sq, 2) * a**2)

            loigiai = ('''Do tất cả các cạnh của hình chóp bằng nhau nên hình chóp $S.ABCD$ là hình chóp đều. \\\\
            Gọi $O$ là tâm của hình vuông $ABCD$, ta có:\\\\
            $\\begin{cases} SO \\perp (ABCD) \\\\ AC \\perp BD \\end{cases}$.\\\\
            Do $M$ là trung điểm của $CD$ nên ta có:\\\\
            $\\vec{MS} = \\vec{OS} - \\vec{OM} = \\vec{OS} - \\frac{1}{2}(\\vec{OC} + \\vec{OD}) = \\vec{OS} - \\frac{1}{2}\\vec{OC} - \\frac{1}{2}\\vec{OD}$.\\\\
            Mặt khác, $\\vec{CB} = \\vec{OB} - \\vec{OC} = -\\vec{OD} - \\vec{OC}$ (vì $O$ là trung điểm của $BD$).\\\\
            Do các cặp vectơ $(\\vec{OC}, \\vec{OS})$, $(\\vec{OS}, \\vec{OD})$, $(\\vec{OC}, \\vec{OD})$ đôi một vuông góc với nhau nên:\\\\
            $\\vec{MS} \\cdot \\vec{CB} = \\left( \\vec{OS} - \\frac{1}{2}\\vec{OC} - \\frac{1}{2}\\vec{OD} \\right) \\cdot (-\\vec{OD} - \\vec{OC})$\\\\
            $= -\\vec{OS}\\cdot\\vec{OD} - \\vec{OS}\\cdot\\vec{OC} + \\frac{1}{2}\\vec{OC}\\cdot\\vec{OD} + \\frac{1}{2}OC^2 + \\frac{1}{2}OD^2 + \\frac{1}{2}\\vec{OD}\\cdot\\vec{OC}$\\\\
            $= \\frac{1}{2}OC^2 + \\frac{1}{2}OD^2$.\\\\
            Vì $ABCD$ là hình vuông cạnh $%s$ nên đường chéo $AC = %s\\sqrt{2}$, suy ra $OC = OD = \\frac{%s\\sqrt{2}}{2}$.\\\\
            Do đó $OC^2 = OD^2 = %s$.\\\\
            Vậy $\\vec{MS} \\cdot \\vec{CB} = \\frac{1}{2} \\cdot %s + \\frac{1}{2} \\cdot %s = %s$.''' 
            % (latex(canh), latex(canh), latex(canh), oc_sq_latex, oc_sq_latex, oc_sq_latex, latex(da_dung)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + 
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

