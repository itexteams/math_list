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


def bt_dang14_p2_b1_c2_hh11(self):
            # Khai báo biến
            # Bước 1: Khởi tạo giá trị ngẫu nhiên cho cạnh a (chọn số chẵn để trung điểm đẹp)
            val_a = random.choice([2, 4, 6])

            # Các ký hiệu sympy
            a_sym = symbols('a')

            # Hình chóp S.ABCD đều cạnh a. 
            # Chiều cao SO = a/sqrt(2)
            # Các cạnh bên = a, các cạnh đáy = a

            # Nội dung câu hỏi
            noidungcauhoi = (r'''Cho hình chóp $S.ABCD$ có đáy là hình vuông tâm $O$ và tất cả các cạnh của hình chóp đều bằng $%s$. Gọi $M, N$ lần lượt là trung điểm các cạnh $SA, AB$.''' 
                             % (latex(val_a)))

            ########################################################################
            # Nhận biết - Câu a: MO và SC song song
            ########################################################################
            # Lời giải: MO là đường trung bình của tam giác SAC
            loigiai_nb_1 = ('''Trong tam giác $SAC$, có $M$ là trung điểm của $SA$ và $O$ là trung điểm của $AC$ (tâm hình vuông). \\\\ Do đó $MO$ là đường trung bình của tam giác $SAC$, suy ra $MO \\parallel SC$.''')

            nb_da_1_d = r'\True Hai đường thẳng $MO$ và $SC$ song song với nhau'
            nb_da_1_s = r'Hai đường thẳng $MO$ và $SC$ chéo nhau'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)
            list_nb_1 = [nb_da_1]
            list_nb_2 = [loigiai_nb_1]

            ########################################################################
            # Thông hiểu - Câu b: Góc giữa MN và SD
            ########################################################################
            # Lời giải: MN // SB nên (MN, SD) = (SB, SD). Tam giác SBD có SB=SD=a, BD=a*sqrt(2) => vuông tại S
            loigiai_th_1 = ('''Vì $N, M$ là trung điểm của $AB, SA$ nên $MN \\parallel SB$. \\\\ Khi đó góc giữa $MN$ và $SD$ bằng góc giữa $SB$ và $SD$. \\\\ Xét tam giác $SBD$ có $SB=SD=%s$ và $BD=%s\\sqrt{2}$. \\\\ Ta thấy $SB^2 + SD^2 = BD^2$, suy ra tam giác $SBD$ vuông tại $S$. \\\\ Vậy góc giữa $MN$ và $SD$ bằng $90^\\circ$.'''
                            % (latex(val_a), latex(val_a)))

            th_da_1_d = r'\True Góc giữa hai đường thẳng $MN$ và $SD$ là $90^\circ$'
            th_da_1_s = r'Góc giữa hai đường thẳng $MN$ và $SD$ là $30^\circ$'
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)
            list_th_1 = [th_da_1]
            list_th_2 = [loigiai_th_1]

            ########################################################################
            # Vận dụng - Câu c: Góc giữa MO và SB
            ########################################################################
            # Lời giải: MO // SC nên (MO, SB) = (SC, SB). Tam giác SBC đều nên góc = 60 độ.
            loigiai_vd_1 = ('''Ta có $MO \\parallel SC$ nên góc giữa $MO$ và $SB$ bằng góc giữa $SC$ và $SB$. \\\\ Vì tất cả các cạnh của hình chóp bằng nhau nên tam giác $SBC$ là tam giác đều, suy ra $\\widehat{BSC} = 60^\\circ$. \\\\ Vậy góc giữa $MO$ và $SB$ bằng $60^\\circ$.''')

            vd_da_1_d = r'\True Góc giữa hai đường thẳng $MO$ và $SB$ là $60^\circ$'
            vd_da_1_s = r'Góc giữa hai đường thẳng $MO$ và $SB$ là $90^\circ$'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)
            list_vd_1 = [vd_da_1]
            list_vd_2 = [loigiai_vd_1]

            ########################################################################
            # Vận dụng cao - Câu d: Tang của góc giữa SN và BC
            ########################################################################
            # Lời giải: BC // AD => (SN, BC) = (SN, AD). Dùng hệ thức lượng hoặc tọa độ tính được tan = sqrt(2)
            loigiai_vdc_1 = ('''Vì $BC \\parallel AD$ nên góc giữa $SN$ và $BC$ bằng góc giữa $SN$ và $AD$. \\\\ Gọi $\\phi$ là góc cần tìm. \\\\ Ta có $SN = \\dfrac{%s\\sqrt{3}}{2}$ (đường cao tam giác đều $SAB$). \\\\ Sử dụng định lý hàm số cos trong tam giác $SND$ (với $DN^2 = AN^2 + AD^2$), ta tính được $\\cos \\phi = \\dfrac{1}{\\sqrt{3}}$. \\\\ Từ đó $\\tan \\phi = \\sqrt{\\dfrac{1}{\\cos^2 \\phi} - 1} = \\sqrt{3-1} = \\sqrt{2}$.'''
                             % (latex(val_a)))

            vdc_da_1_d = r'\True Tang của góc giữa hai đường thẳng $SN$ và $BC$ là $\sqrt{2}$'
            vdc_da_1_s = r'Tang của góc giữa hai đường thẳng $SN$ và $BC$ là $\dfrac{\sqrt{2}}{2}$'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)
            list_vdc_1 = [vdc_da_1]
            list_vdc_2 = [loigiai_vdc_1]

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi đáp án có từ 1 đến 3 câu đúng
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)
                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                if 1 <= count_true_answers(answers) <= 3:
                    break

            # Gán lại và xáo trộn (giữ nguyên logic mẫu)
            combined_nb = list(zip([nb_da_1], list_nb_2)); random.shuffle(combined_nb)
            combined_th = list(zip([th_da_1], list_th_2)); random.shuffle(combined_th)
            combined_vd = list(zip([vd_da_1], list_vd_2)); random.shuffle(combined_vd)
            combined_vdc = list(zip([vdc_da_1], list_vdc_2)); random.shuffle(combined_vdc)

            sh_a_nb, sh_s_nb = zip(*combined_nb)
            sh_a_th, sh_s_th = zip(*combined_th)
            sh_a_vd, sh_s_vd = zip(*combined_vd)
            sh_a_vdc, sh_s_vdc = zip(*combined_vdc)

            # Hình vẽ TikZ
            hinh_ve = r'''
            \begin{center}
            \begin{tikzpicture}[scale=1, font=\footnotesize, line join=round, line cap=round]
            \coordinate (A) at (0,0);
            \coordinate (B) at (1.2,-1.2);
            \coordinate (C) at (3.5,-1.2);
            \coordinate (D) at (2.3,0);
            \coordinate (O) at (1.75,-0.6);
            \coordinate (S) at (1.75,2.5);
            \coordinate (M) at ($(S)!0.5!(A)$);
            \coordinate (N) at ($(A)!0.5!(B)$);
            \draw[dashed] (A)--(D)--(C) (S)--(D) (A)--(C) (B)--(D) (S)--(O) (M)--(O);
            \draw (S)--(A)--(B)--(C)--(S)--(B) (S)--(N);
            \foreach \p/\pos in {S/above, A/left, B/below, C/right, D/right, O/below, M/left, N/below left}
                \filldraw (\p) node[\pos] {$\p$};
            \end{tikzpicture}
            \end{center}'''

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + 
                str(noidungcauhoi) + hinh_ve + 
                '\n\\choiceTFn \n'
                '{' + str(sh_a_nb[0]) + '}\n'
                '{' + str(sh_a_th[0]) + '}\n'
                '{' + str(sh_a_vd[0]) + '}\n'
                '{' + str(sh_a_vdc[0]) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(sh_s_nb[0]) + '\n'
                '\\item ' + str(sh_s_th[0]) + '\n'
                '\\item ' + str(sh_s_vd[0]) + '\n'
                '\\item ' + str(sh_s_vdc[0]) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

