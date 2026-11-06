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


def bt_dang5_p2_b1_c6_ds10(self):
            # Khai báo biến
            # Khai báo biến (không dùng trong bài này nhưng giữ cấu trúc)
            x = symbols('x')

            # Nội dung câu hỏi
            noidungcauhoi = ('Gieo đồng thời hai viên xúc xắc $6$ mặt cân đối và đồng chất.')

            ########################################################################
            # Nhận biết ############################################
            # Các đáp án cho mệnh đề (a)
            nb_da_1_d = '\\True $n(\\Omega)=36$'
            nb_da_1_s = '$n(\\Omega)=12$'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            # Nội dung lời giải mệnh đề (a)
            loigiai_nb_1 = ('Mỗi viên xúc xắc có $6$ khả năng xuất hiện. Vì gieo hai viên xúc xắc nên số phần tử của không gian mẫu là $n(\\Omega) = 6 \\cdot 6 = 36$.')

            list_nb_1 = [nb_da_1]
            list_nb_2 = [loigiai_nb_1]
            combined_nb = list(zip(list_nb_1, list_nb_2))

            ########################################################################
            # Thông hiểu ############################################
            # Các đáp án cho mệnh đề (b)
            th_da_1_d = '\\True Gọi $A$ là biến cố: "Số chấm xuất hiện trên mỗi viên xúc xắc là một số chẵn", khi đó: $n(A)=9$'
            th_da_1_s = 'Gọi $A$ là biến cố: "Số chấm xuất hiện trên mỗi viên xúc xắc là một số chẵn", khi đó: $n(A)=6$'
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            # Nội dung lời giải mệnh đề (b)
            loigiai_th_1 = ('Các số chẵn trên mặt xúc xắc là $\\{2; 4; 6\\}$ ($3$ số). Để mỗi viên đều hiện số chẵn thì có $3 \\cdot 3 = 9$ kết quả. Vậy $n(A)=9$.')

            list_th_1 = [th_da_1]
            list_th_2 = [loigiai_th_1]
            combined_th = list(zip(list_th_1, list_th_2))

            ########################################################################
            # Vận dụng ############################################
            # Các đáp án cho mệnh đề (c)
            vd_da_1_d = '\\True Gọi $B$ là biến cố: "Số chấm xuất hiện trên mỗi viên xúc xắc là một số lẻ", khi đó: $n(B)=9$'
            vd_da_1_s = 'Gọi $B$ là biến cố: "Số chấm xuất hiện trên mỗi viên xúc xắc là một số lẻ", khi đó: $n(B)=3$'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            # Nội dung lời giải mệnh đề (c)
            loigiai_vd_1 = ('Các số lẻ trên mặt xúc xắc là $\\{1; 3; 5\\}$ ($3$ số). Để mỗi viên đều hiện số lẻ thì có $3 \\cdot 3 = 9$ kết quả. Vậy $n(B)=9$.')

            list_vd_1 = [vd_da_1]
            list_vd_2 = [loigiai_vd_1]
            combined_vd = list(zip(list_vd_1, list_vd_2))

            ########################################################################
            # Vận dụng cao ############################################
            # Các đáp án cho mệnh đề (d)
            vdc_da_1_d = '\\True Gọi $C$ là biến cố: "Số chấm xuất hiện trên mỗi viên xúc xắc là bằng nhau", khi đó: $n(C)=6$'
            vdc_da_1_s = 'Gọi $C$ là biến cố: "Số chấm xuất hiện trên mỗi viên xúc xắc là bằng nhau", khi đó: $n(C)=1$'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            # Nội dung lời giải mệnh đề (d)
            loigiai_vdc_1 = ('Biến cố $C$ xảy ra khi kết quả là các cặp $\\left( 1;1 \\right), \\left( 2;2 \\right), \\left( 3;3 \\right), \\left( 4;4 \\right), \\left( 5;5 \\right), \\left( 6;6 \\right)$. Vậy $n(C)=6$.')

            list_vdc_1 = [vdc_da_1]
            list_vdc_2 = [loigiai_vdc_1]
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi đáp án có từ 1 đến 3 đúng
            while True:
                nb_sel = random.choice(list_nb_da_1)
                th_sel = random.choice(list_th_da_1)
                vd_sel = random.choice(list_vd_da_1)
                vdc_sel = random.choice(list_vdc_da_1)

                answers = [nb_sel, th_sel, vd_sel, vdc_sel]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Gán lại giá trị đã chọn
            shuffled_answers_nb = [nb_sel]
            shuffled_answers_th = [th_sel]
            shuffled_answers_vd = [vd_sel]
            shuffled_answers_vdc = [vdc_sel]

            shuffled_solutions_nb = [loigiai_nb_1]
            shuffled_solutions_th = [loigiai_th_1]
            shuffled_solutions_vd = [loigiai_vd_1]
            shuffled_solutions_vdc = [loigiai_vdc_1]

            # Xuất câu hỏi với đáp án và lời giải (Không dùng tiền tố r, dùng \\ cho các ký tự đặc biệt)
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' +
                str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(shuffled_answers_nb[0]) + '}\n'
                '{' + str(shuffled_answers_th[0]) + '}\n'
                '{' + str(shuffled_answers_vd[0]) + '}\n'
                '{' + str(shuffled_answers_vdc[0]) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(shuffled_solutions_nb[0]) + '\n'
                '\\item ' + str(shuffled_solutions_th[0]) + '\n'
                '\\item ' + str(shuffled_solutions_vd[0]) + '\n'
                '\\item ' + str(shuffled_solutions_vdc[0]) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

