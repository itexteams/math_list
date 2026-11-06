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


def bt_dang41_p4_b6_c2_hh11(self):
            # Khai báo biến
            # Với a=5, b=3: 3(25-9) = 48. Các cặp (x, y) thỏa mãn y^2 - x^2 = 48 là (4, 8), (1, 7), (11, 13)
            danh_sach_bo_so = [
                {'a': 5, 'b': 3, 'x': 4, 'y': 8, 'sa': 9},
                {'a': 5, 'b': 3, 'x': 1, 'y': 7, 'sa': 6},
                {'a': 11, 'b': 7, 'x': 8, 'y': 16, 'sa': 12}
            ]

            sel = random.choice(danh_sach_bo_so)
            a_val, b_val, x_val, y_val, sa_val = sel['a'], sel['b'], sel['x'], sel['y'], sel['sa']

            # Tính toán các đại lượng bằng Sympy để giữ nguyên dạng căn thức
            ab_sym = a_val * sqrt(3)
            bc_sym = b_val * sqrt(3)
            ad_sym = Rational(x_val)
            cd_sym = Rational(y_val)
            sa_sym = Rational(sa_val)

            # Diện tích đáy và Thể tích
            s_abcd = Rational(1, 2) * (ab_sym * ad_sym + bc_sym * cd_sym)
            v_abcd = Rational(1, 3) * sa_sym * s_abcd

            # BD và AH
            bd_sq = ab_sym**2 + ad_sym**2
            bd_sym = sqrt(bd_sq)
            ah_sym = (ab_sym * ad_sym) / bd_sym

            # Cotang góc SHA
            cot_val = simplify(ah_sym / sa_sym)

            # Tạo các phương án nhiễu (B4)
            da_dung = '$' + latex(cot_val) + '$'
            sai1 = '$' + latex(simplify(bd_sym / sa_sym)) + '$'
            sai2 = '$' + latex(simplify(sa_sym / ah_sym)) + '$'
            sai3 = '$' + latex(simplify(Rational(a_val, sa_val) * sqrt(3))) + '$'

            # Đảm bảo các phương án không trùng nhau
            list_da = [('\\True ' + da_dung), sai1, sai2, sai3]
            random.shuffle(list_da)

            # Vẽ hình TikZ (B2)
            # Tọa độ các điểm
            tikz_code = (r'''\begin{center}
            	\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            		\draw [line width=1]    (92.47,168.4) -- (212.47,168.4) ;
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (164.47,150.4) -- (164.47,35.4) ;
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (132.47,128.4) -- (252.47,128.4) ;
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (92.47,168.4) -- (132.47,128.4) ;
            		\draw [line width=1]    (212.47,168.4) -- (252.47,128.4) ;
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (132.47,128.4) -- (164.47,150.4) ;
            		\draw [line width=1]    (164.47,35.4) -- (92.47,168.4) ; 
            		\draw [line width=1]    (164.47,35.4) -- (212.47,168.4) ;
            		\draw [line width=1]    (164.47,35.4) -- (252.47,128.4) ;
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (92.47,168.4) -- (252.47,128.4) ;
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (132.47,128.4) -- (164.47,35.4) ;
            		\draw (157,10) node [anchor=north west][inner sep=0.75pt]    {$S$};
            		\draw (118,111) node [anchor=north west][inner sep=0.75pt]    {$A$};
            		\draw (74,166) node [anchor=north west][inner sep=0.75pt]    {$B$};
            		\draw (212.47,168.4) node [anchor=north west][inner sep=0.75pt]    {$C$};
            		\draw (255.47,117.4) node [anchor=north west][inner sep=0.75pt]    {$D$};
            	\end{tikzpicture}
            \end{center}''')

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có $AB = %s$, $BC = %s$, góc $\\widehat{BAD} = \\widehat{BCD} = 90^\\circ$, $SA = %s$ và $SA$ vuông góc với đáy. Biết thể tích khối chóp $S.ABCD$ bằng $%s$, tính cotang của góc giữa mặt phẳng $\\left(SBD\\right)$ và mặt đáy.'''
                            %(latex(ab_sym), latex(bc_sym), latex(sa_sym), latex(v_abcd)))

            # Nội dung lời giải chi tiết
            loigiai = ('''Có: $V_{S.ABCD} = \\frac{1}{3} \\cdot SA \\cdot S_{ABCD} \\Leftrightarrow %s = \\frac{1}{3} \\cdot %s \\cdot S_{ABCD} \\Rightarrow S_{ABCD} = %s$. \\\\
            Suy ra $\\frac{1}{2}AB \\cdot AD + \\frac{1}{2}BC \\cdot CD = %s \\Leftrightarrow \\frac{1}{2} \\cdot %s \\cdot AD + \\frac{1}{2} \\cdot %s \\cdot CD = %s \\Leftrightarrow %s AD + %s CD = %s$ (1). \\\\
            Áp dụng định lí Pitago trong 2 tam giác vuông $ABD, BCD$, ta có: \\\\
            $AB^2 + AD^2 = BD^2 = BC^2 + CD^2 \\Leftrightarrow CD^2 - AD^2 = %s^2 - %s^2 = %s$ (2). \\\\
            Từ (1) và (2) suy ra $AD = %s$ và $CD = %s$. \\\\
            Trong tam giác $ABD$, dựng $AH \\perp BD$, lại có $SA \\perp BD \\Rightarrow BD \\perp \\left(SAH\\right)$. \\\\
            Vậy góc giữa $\\left(SBD\\right)$ và đáy là góc $\\widehat{SHA}$. \\\\
            Dễ tính $BD = \\sqrt{%s^2 + %s^2} = %s$, $AH = \\frac{AB \\cdot AD}{BD} = \\frac{%s \\cdot %s}{%s} = %s$. \\\\
            $\\cot \\widehat{SHA} = \\frac{AH}{SA} = \\frac{%s}{%s} = %s$.'''
                      %(latex(v_abcd), latex(sa_sym), latex(s_abcd), 
                        latex(s_abcd), latex(ab_sym), latex(bc_sym), latex(s_abcd), latex(a_val*3), latex(b_val*3), latex(s_abcd*2*sqrt(3)/3),
                        latex(ab_sym), latex(bc_sym), latex(ab_sym**2 - bc_sym**2), 
                        latex(ad_sym), latex(cd_sym), 
                        latex(ab_sym), latex(ad_sym), latex(bd_sym), 
                        latex(ab_sym), latex(ad_sym), latex(bd_sym), latex(ah_sym), 
                        latex(ah_sym), latex(sa_sym), latex(cot_val)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + 
                '\\loigiai{'+ tikz_code+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

