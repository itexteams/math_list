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


def bt_dang23_p2_b1_c4_ds12(self):
            # Khai báo biến
            # --- Khai báo các hằng số bài toán ---
            n_phan_tu = 12
            an_chia_3 = [3, 6, 9, 12]
            an_chia_5 = [5, 10]
            binh_chan = [2, 4, 6, 8, 10, 12]
            binh_le = [1, 3, 5, 7, 9, 11]

            # Tính toán các giá trị thuận lợi
            n_A = len(an_chia_3) * n_phan_tu  # 4 * 12 = 48
            n_B = len(an_chia_5) * n_phan_tu  # 2 * 12 = 24
            n_C = len(binh_chan) * n_phan_tu  # 6 * 12 = 72
            kg_mau = n_phan_tu * n_phan_tu    # 144

            # Tính xác suất
            p_cond_c = Rational(len(binh_chan), n_phan_tu) # 1/2
            p_cond_d = Rational(len(an_chia_5), n_phan_tu) # 1/6

            # --- Nội dung câu hỏi (Hình vẽ TikZ) ---
            tikz_spinner = r"""\begin{tikzpicture}[scale=0.8, font=\footnotesize]
                \draw[thick] (0,0) circle (2);
                \foreach \i in {1,...,12} {
                    \draw (0,0) -- (90-\i*30+30:2);
                    \node at (90-\i*30+15:1.6) {\i};
                }
                \draw[fill=gray!50, opacity=0.3] (0,0) -- (90:2) arc (90:60:2) -- cycle;
                \draw[-stealth, thick] (0,0) -- (75:1.5);
            \end{tikzpicture}"""

            noidungcauhoi = ('''Một vòng quay được chia thành %s phần bằng nhau và được đánh số từ 1 đến %s như hình vẽ bên dưới:
            \\begin{center}
            %s
            \\end{center}
            Xét phép thử An và Bình lần lượt quay vòng quay trên. Gọi $A$ là biến cố "An quay được số chia hết cho 3"; $B$ là biến cố "An quay được số chia hết cho 5"; $C$ là biến cố "Bình quay được số chẵn".''' 
            % (n_phan_tu, n_phan_tu, tikz_spinner))

            # --- NHẬN BIẾT: Không gian mẫu ---
            nb_da_1_d = '\\True Không gian mẫu của phép thử có số kết quả là %s' % (kg_mau)
            nb_da_1_s = 'Không gian mẫu của phép thử có số kết quả là %s' % (n_phan_tu * 2)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = ('''Số phần tử của không gian mẫu là: $%s \\cdot %s = %s$.''' % (n_phan_tu, n_phan_tu, kg_mau))

            # --- THÔNG HIỂU: Số kết quả thuận lợi ---
            th_da_1_d = '\\True Số kết quả thuận lợi cho biến cố $A, B, C$ lần lượt là %s, %s, %s' % (n_A, n_B, n_C)
            th_da_1_s = 'Số kết quả thuận lợi cho biến cố $A, B, C$ lần lượt là %s, %s, %s' % (len(an_chia_3), len(an_chia_5), len(binh_chan))
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = ('''
            - Số An quay được chia hết cho 3 nên có %s cách chọn, còn Bình có %s cách chọn. Do đó số kết quả thuận lợi cho biến cố $A$ là: $%s \\cdot %s = %s$. \\\\
            - Số An quay được chia hết cho 5 nên có %s cách chọn, còn Bình có %s cách chọn. Do đó số kết quả thuận lợi cho biến cố $B$ là: $%s \\cdot %s = %s$. \\\\
            - Số Bình quay được là chẵn nên có %s cách chọn, còn An có %s cách chọn. Do đó số kết quả thuận lợi cho biến cố $C$ là: $%s \\cdot %s = %s$.''' 
            % (len(an_chia_3), n_phan_tu, len(an_chia_3), n_phan_tu, n_A,
               len(an_chia_5), n_phan_tu, len(an_chia_5), n_phan_tu, n_B,
               len(binh_chan), n_phan_tu, len(binh_chan), n_phan_tu, n_C))

            # --- VẬN DỤNG: Xác suất có điều kiện (Bình chẵn | An chia 3) ---
            vd_da_1_d = '\\True Xác suất để Bình quay được số chẵn, biết An quay được số chia hết cho 3 là $%s$' % (latex(p_cond_c))
            vd_da_1_s = 'Xác suất để Bình quay được số chẵn, biết An quay được số chia hết cho 3 là $%s$' % (latex(p_cond_d))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = ('''Gọi $A$ là biến cố "An quay được số chia hết cho 3", $C$ là biến cố "Bình quay được số chẵn". \\\\
            Xác suất cần tìm là $P(C|A)$. Do An và Bình quay là độc lập ở hai lần quay khác nhau nên $P(C|A) = P(C)$. \\\\
            Ta có $C = \\{%s\\} \\Rightarrow P(C) = \\frac{%s}{%s} = %s$.''' 
            % (', '.join(map(str, binh_chan)), len(binh_chan), n_phan_tu, latex(p_cond_c)))

            # --- VẬN DỤNG CAO: Xác suất có điều kiện (An chia 5 | Bình lẻ) ---
            vdc_da_1_d = '\\True Xác suất để An quay được số chia hết cho 5, biết Bình quay được số lẻ là $%s$' % (latex(p_cond_d))
            vdc_da_1_s = 'Xác suất để An quay được số chia hết cho 5, biết Bình quay được số lẻ là $%s$' % (latex(Rational(1, n_phan_tu)))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = ('''Gọi $X$ là biến cố "An quay được số chia hết cho 5", $\\overline{C}$ là biến cố "Bình quay được số lẻ". \\\\
            Xác suất cần tìm là $P(X|\\overline{C})$. Do An và Bình quay độc lập nên $P(X|\\overline{C}) = P(X)$. \\\\
            Ta có $X = \\{%s\\} \\Rightarrow P(X) = \\frac{n(X)}{n(\\Omega)} = \\frac{%s}{%s} = %s$.''' 
            % (', '.join(map(str, an_chia_5)), len(an_chia_5), n_phan_tu, latex(p_cond_d)))

            # --- Xử lý chọn ngẫu nhiên và xuất nội dung ---
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                nb_da = random.choice(list_nb_da_1)
                th_da = random.choice(list_th_da_1)
                vd_da = random.choice(list_vd_da_1)
                vdc_da = random.choice(list_vdc_da_1)
                if 1 <= count_true_answers([nb_da, th_da, vd_da, vdc_da]) <= 3:
                    break

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + 
                '\n\\choiceTFn \n'
                '{' + str(nb_da) + '}\n'
                '{' + str(th_da) + '}\n'
                '{' + str(vd_da) + '}\n'
                '{' + str(vdc_da) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_nb_1) + '\n'
                '\\item ' + str(loigiai_th_1) + '\n'
                '\\item ' + str(loigiai_vd_1) + '\n'
                '\\item ' + str(loigiai_vdc_1) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

