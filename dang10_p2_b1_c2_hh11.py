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


def bt_dang10_p2_b1_c2_hh11(self):
            # Khai báo biến
            # Phần này vẫn dùng r''' để viết mã TikZ cho gọn, không ảnh hưởng đến phần content bên dưới
            noidungcauhoi = r'''Cho hình hộp $ABCD.A'B'C'D'$ có tất cả các cạnh đều bằng nhau.
            \begin{center}
            \begin{tikzpicture}[line join=round, line cap=round, >=stealth, scale=0.8]
              \coordinate (A) at (0,0);
              \coordinate (B) at (3,0);
              \coordinate (D) at (1.2,1.2);
              \coordinate (C) at ($(B)+(D)-(A)$);
              \coordinate (A1) at (0.5,3.5);
              \coordinate (B1) at ($(A1)+(B)-(A)$);
              \coordinate (D1) at ($(A1)+(D)-(A)$);
              \coordinate (C1) at ($(A1)+(C)-(A)$);
              \draw (A1)--(B1)--(C1)--(D1)--cycle;
              \draw (B1)--(B)--(C)--(C1);
              \draw  (A1)--(A)--(B);
              \draw[dashed] (C)--(D) (A)--(D)--(D1);
              \foreach \p/\l/\pos in {A/A/left, B/B/right, C/C/right, D/D/above, A1/A'/left, B1/B'/right, C1/C'/right, D1/D'/above}
              \node[\pos] at (\p) {$\l$};
            \end{tikzpicture}
            \end{center}'''

            ########################################################################
            # Nhận biết - Mệnh đề a
            nb_da_1_d = '\\True $ABCD$ là hình thoi'
            nb_da_1_s = '$ABCD$ là hình chữ nhật'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1_d = 'Vì hình hộp có tất cả các cạnh bằng nhau nên tứ giác đáy $ABCD$ có 4 cạnh bằng nhau, suy ra $ABCD$ là hình thoi.'
            loigiai_nb_1_s = 'Hình hộp có các cạnh bằng nhau thì đáy là hình thoi. Nó chỉ là hình chữ nhật khi các cạnh vuông góc (không có giả thiết).'

            ########################################################################
            # Thông hiểu - Mệnh đề b
            th_da_1_d = '\\True $A\'C\' \\perp BD$'
            th_da_1_s = '$A\'C\' \\parallel BD$'
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1_d = 'Ta có $A\'C\' \\parallel AC$ (tính chất hình hộp). Vì $ABCD$ là hình thoi nên $AC \\perp BD$. Suy ra $A\'C\' \\perp BD$.'
            loigiai_th_1_s = '$A\'C\'$ và $BD$ lần lượt song song với hai đường chéo của hình thoi đáy, do đó chúng vuông góc chứ không song song.'

            ########################################################################
            # Vận dụng - Mệnh đề c
            vd_da_1_d = '\\True $A\'B \\perp DC\'$'
            vd_da_1_s = '$A\'B \\parallel DC\'$'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1_d = 'Ta có $A\'B \\parallel D\'C$. Xét mặt bên $DCC\'D\'$ là hình thoi nên $D\'C \\perp DC\'$. Do đó $A\'B \\perp DC\'$.'
            loigiai_vd_1_s = '$A\'B$ song song với $D\'C$, mà $D\'C \\perp DC\'$ nên $A\'B$ phải vuông góc với $DC\'$.'

            ########################################################################
            # Vận dụng cao - Mệnh đề d
            vdc_da_1_d = '\\True $BC\' \\perp A\'D$'
            vdc_da_1_s = '$BC\' \\parallel A\'D$'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1_d = 'Ta có $BC\' \\parallel AD\'$. Xét mặt bên $ADD\'A\'$ là hình thoi nên $AD\' \\perp A\'D$. Do đó $BC\' \\perp A\'D$.'
            loigiai_vdc_1_s = 'Vì $BC\' \\parallel AD\'$ và $AD\' \\perp A\'D$ nên $BC\' \\perp A\'D$.'

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi đáp án có từ 1 đến 3 đúng
            while True:
                ans_a = random.choice(list_nb_da_1)
                ans_b = random.choice(list_th_da_1)
                ans_c = random.choice(list_vd_da_1)
                ans_d = random.choice(list_vdc_da_1)

                answers = [ans_a, ans_b, ans_c, ans_d]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Khớp lời giải
            sol_a = loigiai_nb_1_d if '\\True' in ans_a else loigiai_nb_1_s
            sol_b = loigiai_th_1_d if '\\True' in ans_b else loigiai_th_1_s
            sol_c = loigiai_vd_1_d if '\\True' in ans_c else loigiai_vd_1_s
            sol_d = loigiai_vdc_1_d if '\\True' in ans_d else loigiai_vdc_1_s

            shuffled_answers = [ans_a, ans_b, ans_c, ans_d]
            shuffled_solutions = [sol_a, sol_b, sol_c, sol_d]

            # B3: Xuất nội dung (Phần content KHÔNG dùng tiền tố r)
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' +
                str(noidungcauhoi) + 
                '\n\\choiceTFn \n'
                '{' + str(shuffled_answers[0]) + '}\n'
                '{' + str(shuffled_answers[1]) + '}\n'
                '{' + str(shuffled_answers[2]) + '}\n'
                '{' + str(shuffled_answers[3]) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(shuffled_solutions[0]) + '\n'
                '\\item ' + str(shuffled_solutions[1]) + '\n'
                '\\item ' + str(shuffled_solutions[2]) + '\n'
                '\\item ' + str(shuffled_solutions[3]) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

