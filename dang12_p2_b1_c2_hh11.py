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


def bt_dang12_p2_b1_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến
            a_val = random.randint(2, 10)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hình hộp $ABCD.A'B'C'D'$ có $6$ mặt là hình vuông cạnh $a=%s$.''' 
                             %(latex(a_val)))

            ########################################################################
            # Nhận biết - Câu a
            nb_da_1_d = '\\True $BC\' \\parallel AD\'$'
            nb_da_1_s = '$BC\' \\perp AD\'$'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = ('''Vì $ABCD.A'B'C'D'$ là hình lập phương nên mặt $(ADD'A') \\parallel (BCC'B')$. \\\\
                            Xét tứ giác $ABC'D'$ có $AB \\parallel D'C'$ và $AB = D'C' = %s$, suy ra $ABC'D'$ là hình bình hành. \\\\
                            Do đó $BC' \\parallel AD'$.''' %(latex(a_val)))

            list_nb_2 = [loigiai_nb_1]

            ########################################################################
            # Thông hiểu - Câu b
            th_da_1_d = '\\True $(AD\', B\'C) = 90^\\circ$'
            th_da_1_s = '$(AD\', B\'C) = 45^\\circ$'
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = ('''Ta có $AD' \\parallel BC'$ (theo câu a). \\\\
                            Khi đó $(AD', B'C) = (BC', B'C)$. \\\\
                            Vì $BCC'B'$ là hình vuông nên hai đường chéo $BC' \\perp B'C$. \\\\
                            Vậy $(AD', B'C) = 90^\\circ$.''')

            list_th_2 = [loigiai_th_1]

            ########################################################################
            # Vận dụng - Câu c
            vd_da_1_d = '\\True $(AD\', DC\') = (BC\', DC\')$'
            vd_da_1_s = '$(AD\', DC\') \\neq (BC\', DC\')$'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = ('''Do $AD' \\parallel BC'$ nên góc giữa $AD'$ và $DC'$ bằng góc giữa $BC'$ và $DC'$. \\\\
                            Vậy $(AD', DC') = (BC', DC')$.''')

            list_vd_2 = [loigiai_vd_1]

            ########################################################################
            # Vận dụng cao - Câu d
            vdc_da_1_d = '\\True $\\widehat{BC\'D} = 60^\\circ$'
            vdc_da_1_s = '$\\widehat{BC\'D} = 90^\\circ$'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = ('''Xét tam giác $BC'D$, ta có: \\\\
                            $BC' = \\sqrt{BC^2 + CC'^2} = %s\\sqrt{2}$. \\\\
                            $C'D = \\sqrt{C'D'^2 + D'D^2} = %s\\sqrt{2}$. \\\\
                            $BD = \\sqrt{AB^2 + AD^2} = %s\\sqrt{2}$. \\\\
                            Suy ra $BC' = C'D = BD$, nên $\\triangle BC'D$ là tam giác đều. \\\\
                            Vậy $\\widehat{BC'D} = 60^\\circ$.''' %(latex(a_val), latex(a_val), latex(a_val)))

            list_vdc_2 = [loigiai_vdc_1]

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi đáp án có từ 1 đến 3 đúng
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)
                if 1 <= true_count <= 3:
                    break

            # Gán lại và trộn (tương tự mẫu)
            combined_nb = list(zip([nb_da_1], list_nb_2))
            combined_th = list(zip([th_da_1], list_th_2))
            combined_vd = list(zip([vd_da_1], list_vd_2))
            combined_vdc = list(zip([vdc_da_1], list_vdc_2))

            # Hình vẽ TikZ cho hình lập phương
            hinhve = '''\\begin{center}
            \\begin{tikzpicture}[scale=0.8, line join=round, line cap=round]
            \\coordinate (A) at (0,0);
            \\coordinate (B) at (3,0);
            \\coordinate (D) at (1.2,1.2);
            \\coordinate (C) at ($(B)+(D)-(A)$);
            \\coordinate (A1) at (0,3);
            \\coordinate (B1) at (3,3);
            \\coordinate (D1) at (1.2,4.2);
            \\coordinate (C1) at ($(B1)+(D1)-(A1)$);
            \\draw (A)--(B)--(C)--(C1)--(D1)--(A1)--cycle (A1)--(B1)--(C1) (B1)--(B);
            \\draw[dashed] (A)--(D)--(C) (D)--(D1);
            \\draw[blue, thick] (B)--(C1); \\draw[red, thick, dashed] (A)--(D1);
            \\node[below left] at (A) {$A$}; \\node[below right] at (B) {$B$};
            \\node[right] at (C) {$C$}; \\node[above left] at (D) {$D$};
            \\node[left] at (A1) {$A'$}; \\node[above left] at (B1) {$B'$};
            \\node[above right] at (C1) {$C'$}; \\node[above] at (D1) {$D'$};
            \\end{tikzpicture}
            \\end{center}'''

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n' + hinhve + '\n'
                '\\choiceTFn \n'
                '{' + str(nb_da_1) + '}\n'
                '{' + str(th_da_1) + '}\n'
                '{' + str(vd_da_1) + '}\n'
                '{' + str(vdc_da_1) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_nb_1) + '\n'
                '\\item ' + str(loigiai_th_1) + '\n'
                '\\item ' + str(loigiai_vd_1) + '\n'
                '\\item ' + str(loigiai_vdc_1) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

