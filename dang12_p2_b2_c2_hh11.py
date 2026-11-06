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


def bt_dang12_p2_b2_c2_hh11(self):
            # Khai báo biến
            # Khai báo các biến ký hiệu (không dùng cho tính toán số nhưng dùng để đồng bộ latex nếu cần)
            O, A, B, C, H = symbols('O A B C H')

            # --- B1 & B2: Nội dung câu hỏi và lời giải chi tiết ---
            noidungcauhoi = 'Cho tứ diện $OABC$ có $OA, OB, OC$ đôi một vuông góc. Kẻ $OH \\perp (ABC)$ tại $H$.'

            # --- B3: Thiết lập Random cho các mệnh đề ---

            # Mệnh đề (a): Tính vuông góc của các cạnh đối diện (Luôn Đúng)
            a_d = '\\True $OA \\perp BC, OB \\perp AC, OC \\perp AB$'
            a_s = '$OA // BC, OB // AC, OC // AB$'
            list_a = [a_d, a_s]
            sel_a = random.choice(list_a)
            loigiai_a = 'Vì $OA \\perp OB$ và $OA \\perp OC$ nên $OA \\perp (OBC)$. Mà $BC \\subset (OBC)$ nên $OA \\perp BC$. \\\\ Tương tự ta có $OB \\perp AC$ và $OC \\perp AB$.'

            # Mệnh đề (b): Tính chất góc của tam giác ABC (Luôn Đúng là nhọn)
            b_d = '\\True Tam giác $ABC$ có ba góc nhọn'
            b_s = 'Tam giác $ABC$ có ba góc tù'
            list_b = [b_d, b_s]
            sel_b = random.choice(list_b)
            loigiai_b = 'Gọi $OA=a, OB=b, OC=c$. \\\\Ta có $AB^2=a^2+b^2, AC^2=a^2+c^2, BC^2=b^2+c^2$. \\\\Xét $\\cos \\widehat{BAC} = \\frac{AB^2+AC^2-BC^2}{2AB \\cdot AC} = \\frac{2a^2}{2AB \\cdot AC} > 0$. \\\\Do đó các góc đều nhọn.'

            # Mệnh đề (c): Vị trí điểm H (Đúng là trực tâm, Sai là trọng tâm)
            c_d = '\\True $H$ là trực tâm của tam giác $ABC$'
            c_s = '$H$ là trọng tâm của tam giác $ABC$'
            list_c = [c_d, c_s]
            sel_c = random.choice(list_c)
            loigiai_c = 'Vì $OA \\perp BC$ và $OH \\perp BC$ (do $OH \\perp (ABC)$) nên $BC \\perp (OAH) \\Rightarrow BC \\perp AH$. \\\\Tương tự $AC \\perp BH$. \\\\Vậy $H$ là trực tâm tam giác $ABC$.'

            # Mệnh đề (d): Hệ thức lượng trong tứ diện vuông (Luôn Đúng)
            d_d = '\\True $\\frac{1}{OH^2} = \\frac{1}{OA^2} + \\frac{1}{OB^2} + \\frac{1}{OC^2}$'
            d_s = '$\\frac{1}{OH} = \\frac{1}{OA} + \\frac{1}{OB} + \\frac{1}{OC}$'
            list_d = [d_d, d_s]
            sel_d = random.choice(list_d)
            loigiai_d = 'Kẻ $OK \\perp BC$ tại $K$. Ta có $OA \\perp (OBC) \\Rightarrow OA \\perp BC$. \\\\Suy ra $BC \\perp (OAK)$. \\\\Khi đó $OH$ là đường cao trong tam giác vuông $OAK$: $\\frac{1}{OH^2} = \\frac{1}{OA^2} + \\frac{1}{OK^2}$. \\\\ Mà $\\frac{1}{OK^2} = \\frac{1}{OB^2} + \\frac{1}{OC^2}$. Vậy $\\frac{1}{OH^2} = \\frac{1}{OA^2} + \\frac{1}{OB^2} + \\frac{1}{OC^2}$.'

            # --- Xử lý chọn lọc để đảm bảo có từ 1 đến 3 đáp án đúng ---
            def count_true(ans_list):
                return sum('\\True' in ans for ans in ans_list)

            while True:
                a_f = random.choice(list_a)
                b_f = random.choice(list_b)
                c_f = random.choice(list_c)
                d_f = random.choice(list_d)

                current_answers = [a_f, b_f, c_f, d_f]
                if 1 <= count_true(current_answers) <= 3:
                    break

            # --- Vẽ hình TikZ (Độ dày 1pt, giống hình mẫu) ---
            hinh_ve = r'''\begin{center}
            	\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (103.47,139.69) -- (278.32,139.69) ;
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (103.47,139.69) -- (103.47,30.4) ;
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (103.47,139.69) -- (78.47,201.4) ;
            		\draw [line width=1]    (78.47,201.4) -- (278.32,139.69) ;
            		\draw [line width=1]    (103.47,30.4) -- (278.32,139.69) ;
            		\draw [line width=1]    (103.47,30.4) -- (78.47,201.4) ;
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (103.47,139.69) -- (170.47,172.4) ;
            		\draw [line width=1]    (103.47,30.4) -- (170.47,172.4) ;
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (142.47,111.4) -- (103.47,139.69) ;
            		\draw [line width=1]    (78.47,201.4) -- (169.47,71.4) ;
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (169.47,71.4) -- (103.47,139.69) ;
            		\draw (89,126) node [anchor=north west][inner sep=0.75pt]    {$O$};
            		\draw (279,129) node [anchor=north west][inner sep=0.75pt]    {$B$};
            		\draw (67,202) node [anchor=north west][inner sep=0.75pt]    {$C$};
            		\draw (94,5) node [anchor=north west][inner sep=0.75pt]    {$A$};
            		\draw (145,100) node [anchor=north west][inner sep=0.75pt]    {$H$};
            		\draw (170.47,172.4) node [anchor=north west][inner sep=0.75pt]    {$K$};
            		\draw (170,50) node [anchor=north west][inner sep=0.75pt]    {$E$};
            	\end{tikzpicture}
            \end{center}'''

            # --- Xuất nội dung theo mẫu ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + 
                str(noidungcauhoi) + 
                '\\choiceTFn \n'
                '{' + str(a_f) + '}\n'
                '{' + str(b_f) + '}\n'
                '{' + str(c_f) + '}\n'
                '{' + str(d_f) + '}\n'
                '\\loigiai{ \n'
                +hinh_ve+
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_a) + '\n'
                '\\item ' + str(loigiai_b) + '\n'
                '\\item ' + str(loigiai_c) + '\n'
                '\\item ' + str(loigiai_d) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

