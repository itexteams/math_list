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


def bt_dang19_p2_b1_c2_hh11(self):
            # Khai báo biến
            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hình lập phương $ABCD.A'B'C'D'$.''')

            ########################################################################
            # Nhận biết - Mệnh đề (a): Về tính song song
            ########################################################################
            # Các đáp án
            nb_da_1_d = '\\True $BD // B\'D\'$'
            nb_da_1_s = '$BD$ và $B\'D\'$ chéo nhau'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            # Lời giải
            loigiai_nb_1 = ('''Trong hình lập phương $ABCD.A'B'C'D'$, mặt phẳng $(ABCD) // (A'B'C'D')$. 
            Các đường thẳng $BD$ và $B'D'$ là các đường chéo tương ứng của hai mặt đối diện song song, do đó $BD // B'D'$.''')

            list_nb_2 = [loigiai_nb_1]
            combined_nb = list(zip([nb_da_1], list_nb_2))
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu - Mệnh đề (b): Góc giữa hai đường thẳng AC và B'D'
            ########################################################################
            # Các đáp án
            th_da_1_d = '\\True $(AC, B\'D\') = 90^\\circ$'
            th_da_1_s = '$(AC, B\'D\') = 45^\\circ$'
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            # Lời giải
            loigiai_th_1 = ('''Vì $BD // B'D'$ nên $(AC, B'D') = (AC, BD)$. 
            Mà $ABCD$ là hình vuông nên hai đường chéo $AC \\perp BD$. Suy ra $(AC, B'D') = 90^\\circ$.''')

            list_th_2 = [loigiai_th_1]
            combined_th = list(zip([th_da_1], list_th_2))
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ########################################################################
            # Vận dụng - Mệnh đề (c): Tính chất tam giác ACD'
            ########################################################################
            # Các đáp án
            vd_da_1_d = '\\True Tam giác $ACD\'$ đều'
            vd_da_1_s = 'Tam giác $ACD\'$ vuông tại $D\'$'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            # Lời giải
            loigiai_vd_1 = ('''Xét tam giác $ACD'$, ta có: \\\\
            $AC$ là đường chéo mặt $(ABCD)$ \\\\
            $CD'$ là đường chéo mặt $(CDD'C')$ \\\\
            $AD'$ là đường chéo mặt $(ADD'A')$ \\\\
            Vì tất cả các mặt của hình lập phương là các hình vuông bằng nhau nên $AC = CD' = AD'$. 
            Vậy tam giác $ACD'$ đều.''')

            list_vd_2 = [loigiai_vd_1]
            combined_vd = list(zip([vd_da_1], list_vd_2))
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ########################################################################
            # Vận dụng cao - Mệnh đề (d): Góc giữa AC và A'B
            ########################################################################
            # Các đáp án
            vdc_da_1_d = '$(AC, A\'B) = 30^\\circ$' # Câu này sai trong đề gốc
            vdc_da_2_d = '\\True $(AC, A\'B) = 60^\\circ$'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_2_d]
            vdc_da_1 = random.choice(list_vdc_da_1)

            # Lời giải
            loigiai_vdc_1 = ('''Ta có $AC // A'C'$, do đó $(AC, A'B) = (A'C', A'B)$. \\\\
            Xét tam giác $A'BC'$, ta có $A'B, BC', C'A'$ đều là các đường chéo của các mặt hình lập phương. \\\\
            Do đó $A'B = BC' = C'A'$, suy ra tam giác $A'BC'$ đều, dẫn đến $\\widehat{BA'C'} = 60^\\circ$. \\\\
            Vậy $(AC, A'B) = 60^\\circ$.''')

            list_vdc_2 = [loigiai_vdc_1]
            combined_vdc = list(zip([vdc_da_1], list_vdc_2))
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Vòng lặp đảm bảo số câu đúng từ 1 đến 3
            while True:
                nb_da = random.choice(list_nb_da_1)
                th_da = random.choice(list_th_da_1)
                vd_da = random.choice(list_vd_da_1)
                vdc_da = random.choice(list_vdc_da_1)

                answers = [nb_da, th_da, vd_da, vdc_da]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Vẽ hình bằng TikZ
            hinh_ve = ('''\\begin{tikzpicture}[scale=0.8, line join=round, line cap=round]
            \\coordinate (A) at (0,0);
            \\coordinate (B) at (3,0);
            \\coordinate (D) at (1.2,1.2);
            \\coordinate (C) at (4.2,1.2);
            \\coordinate (A1) at (0,3);
            \\coordinate (B1) at (3,3);
            \\coordinate (D1) at (1.2,4.2);
            \\coordinate (C1) at (4.2,4.2);
            \\draw (A)--(B)--(C)--(C1)--(D1)--(A1)--cycle;
            \\draw (A1)--(B1)--(C1);
            \\draw (B)--(B1);
            \\draw[dashed] (A)--(D)--(C);
            \\draw[dashed] (D)--(D1);
            \\draw[dashed] (A)--(C);
            \\draw[dashed] (B)--(D);
            \\draw (B1)--(D1);
            \\draw (A1)--(B);
            \\node[below left] at (A) {$A$};
            \\node[below right] at (B) {$B$};
            \\node[right] at (C) {$C$};
            \\node[above left] at (D) {$D$};
            \\node[left] at (A1) {$A'$};
            \\node[below] at (B1) {$B'$};
            \\node[above right] at (C1) {$C'$};
            \\node[above] at (D1) {$D'$};
            \\end{tikzpicture}''')

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' +
                str(noidungcauhoi) + '\n' +
                '\\begin{center}\n' + hinh_ve + '\n\\end{center}\n' +
                '\\choiceTFn \n'
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

