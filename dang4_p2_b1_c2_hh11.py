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


def bt_dang4_p2_b1_c2_hh11(self):
            # Khai báo biến
            # Nội dung câu hỏi
            noidungcauhoi = r'''Cho hình lập phương $ABCD.A'B'C'D'$.'''

            ########################################################################
            # Nhận biết - Mệnh đề a)
            ########################################################################
            # Các đáp án
            nb_da_1_d = r'''\True $BD \parallel B'D'$ '''
            nb_da_1_s = r'''$BD$ và $B'D'$ là hai đường thẳng chéo nhau'''
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            # Lời giải
            loigiai_nb_1 = (r'''Trong hình lập phương $ABCD \cdot A'B'C'D'$, ta có $BD \parallel B'D'$ vì $BDD'B'$ là hình chữ nhật (do $BB' \parallel DD'$ và $BB' = DD'$).''')

            list_nb_1 = [nb_da_1]
            list_nb_2 = [loigiai_nb_1]
            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu - Mệnh đề b)
            ########################################################################
            # Các đáp án
            th_da_1_d = r'''\True $(AC, B'D') = 90^\circ$'''
            th_da_1_s = r'''$(AC, B'D') = 60^\circ$'''
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            # Lời giải
            loigiai_th_1 = (r'''Ta có $AC \parallel A'C'$. Mà $A'C' \perp B'D'$ (hai đường chéo của hình vuông $A'B'C'D'$). Suy ra $AC \perp B'D'$, do đó $(AC, B'D') = 90^\circ$.''')

            list_th_1 = [th_da_1]
            list_th_2 = [loigiai_th_1]
            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ########################################################################
            # Vận dụng - Mệnh đề c)
            ########################################################################
            # Các đáp án
            vd_da_1_d = r'''\True Tam giác $ACD'$ là tam giác đều'''
            vd_da_1_s = r'''Tam giác $ACD'$ là tam giác vuông cân tại $A$'''
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            # Lời giải
            loigiai_vd_1 = (r'''Xét tam giác $ACD'$, ta có: $AC$, $CD'$, $D'A$ lần lượt là các đường chéo của các mặt hình vuông $ABCD$, $CDD'C'$, $ADD'A'$. Vì các mặt của hình lập phương là các hình vuông bằng nhau nên $AC = CD' = D'A$. Vậy tam giác $ACD'$ đều.''')

            list_vd_1 = [vd_da_1]
            list_vd_2 = [loigiai_vd_1]
            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ########################################################################
            # Vận dụng cao - Mệnh đề d)
            ########################################################################
            # Các đáp án
            vdc_da_1_d = r'''\True $(AC, A'B) = 60^\circ$'''
            vdc_da_1_s = r'''$(AC, A'B) = 30^\circ$''' # Đây là mệnh đề Sai trong ảnh
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            # Lời giải
            loigiai_vdc_1 = (r'''Ta có $A'B \parallel D'C$. Khi đó góc giữa $AC$ và $A'B$ bằng góc giữa $AC$ và $D'C$, chính là $\widehat{ACD'}$. Vì tam giác $ACD'$ đều (chứng minh ở câu c) nên $\widehat{ACD'} = 60^\circ$. Vậy $(AC, A'B) = 60^\circ$.''')

            list_vdc_1 = [vdc_da_1]
            list_vdc_2 = [loigiai_vdc_1]
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))
            random.shuffle(combined_vdc)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi đáp án có từ 1 đến 3 đúng để tạo tính ngẫu nhiên cho đề bài
            while True:
                nb_sel = random.choice(list_nb_da_1)
                th_sel = random.choice(list_th_da_1)
                vd_sel = random.choice(list_vd_da_1)
                vdc_sel = random.choice(list_vdc_da_1)

                answers = [nb_sel, th_sel, vd_sel, vdc_sel]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Gán lại kết quả đã chọn vào luồng xuất
            final_answers = [nb_sel, th_sel, vd_sel, vdc_sel]
            final_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

            # Xuất nội dung theo cấu trúc yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' +
                str(noidungcauhoi) + '\n'
                '\\begin{center}\n'
                '\\begin{tikzpicture}[scale=0.8, line join=round, line cap=round]\n'
                '\\coordinate (A) at (0,0); \\coordinate (B) at (3,0); \\coordinate (D) at (1.2,1.2); \\coordinate (C) at ($(B)+(D)-(A)$);\n'
                '\\coordinate (A1) at (0,3); \\coordinate (B1) at (3,3); \\coordinate (D1) at (1.2,4.2); \\coordinate (C1) at (4.2,4.2);\n'
                '\\draw (A1)--(B1)--(C1)--(D1)--cycle; \\draw (A1)--(A)--(B)--(B1) (C1)--(C)--(B);\n'
                '\\draw[dashed] (A)--(D)--(C) (B)--(D) (D)--(D1);\n'
                '\\draw (B1)--(D1); % Minh họa câu a\n'
                '\\node[left] at (A) {$A$}; \\node[below] at (B) {$B$}; \\node[right] at (C) {$C$}; \\node[above right] at (D) {$D$};\n'
                '\\node[left] at (A1) {$A\'$}; \\node[below] at (B1) {$B\'$}; \\node[right] at (C1) {$C\'$}; \\node[above right] at (D1) {$D\'$};\n'
                '\\end{tikzpicture}\n'
                '\\end{center}\n'
                '\\choiceTFn \n'
                '{' + str(final_answers[0]) + '}\n'
                '{' + str(final_answers[1]) + '}\n'
                '{' + str(final_answers[2]) + '}\n'
                '{' + str(final_answers[3]) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(final_solutions[0]) + '\n'
                '\\item ' + str(final_solutions[1]) + '\n'
                '\\item ' + str(final_solutions[2]) + '\n'
                '\\item ' + str(final_solutions[3]) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

