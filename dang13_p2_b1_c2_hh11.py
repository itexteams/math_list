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


def bt_dang13_p2_b1_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến và hằng số ngẫu nhiên
            a_val = randint(2, 6) 

            # Nội dung câu hỏi và hình vẽ TikZ
            noidungcauhoi = (r'''Cho hình chóp $S.ABCD$ có đáy là hình thoi cạnh $a=%s$, $SA = %s\sqrt{3}$, $SA \perp AC$, $SA \perp BC$, $\widehat{BAD} = 120^\circ$. Gọi $M, N$ lần lượt là trung điểm của $AD, BC$ và $I, J$ lần lượt là trung điểm của $SA, SC$.
            \begin{center}
            \begin{tikzpicture}[scale=0.8, line join=round, line cap=round]
            \coordinate (A) at (0,0);
            \coordinate (D) at (4,0);
            \coordinate (B) at (-1.5,-1.5);
            \coordinate (C) at ($(B)+(D)-(A)$);
            \coordinate (S) at (0,4);
            \coordinate (M) at ($(A)!0.5!(D)$);
            \coordinate (N) at ($(B)!0.5!(C)$);
            \coordinate (I) at ($(S)!0.5!(A)$);
            \coordinate (J) at ($(S)!0.5!(C)$);
            \draw [dashed] (S)--(A)--(D) (A)--(B) (I)--(J) (M)--(N);
            \draw (S)--(B)--(C)--(D)--(S) (S)--(C);
            \draw [fill=black] (A) node[left] {$A$};
            \draw [fill=black] (B) node[below left] {$B$};
            \draw [fill=black] (C) node[below right] {$C$};
            \draw [fill=black] (D) node[right] {$D$};
            \draw [fill=black] (S) node[above] {$S$};
            \draw [fill=black] (M) node[above] {$M$};
            \draw [fill=black] (N) node[below] {$N$};
            \draw [fill=black] (I) node[left] {$I$};
            \draw [fill=black] (J) node[right] {$J$};
            \end{tikzpicture}
            \end{center}''' % (a_val, a_val))

            ########################################################################
            # Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = r'\True Góc giữa hai đường thẳng $SD$ và $BC$ là $60^\circ$'
            nb_da_1_s = r'Góc giữa hai đường thẳng $SD$ và $BC$ là $45^\circ$'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = (r'''Vì $BC \parallel AD$ nên $(SD, BC) = (SD, AD) = \widehat{SDA}$. \\ Tam giác $SAD$ vuông tại $A$ có $\tan \widehat{SDA} = \frac{SA}{AD} = \frac{%s\sqrt{3}}{%s} = \sqrt{3} \Rightarrow \widehat{SDA} = 60^\circ$.''' % (a_val, a_val))
            list_nb_2 = [loigiai_nb_1]

            # Kết hợp và xáo trộn
            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = r'\True Góc giữa hai đường thẳng $IJ$ và $BD$ là $90^\circ$'
            th_da_1_s = r'Góc giữa hai đường thẳng $IJ$ và $BD$ là $60^\circ$'
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = (r'''Vì $I, J$ là trung điểm $SA, SC$ nên $IJ \parallel AC$. \\ Trong hình thoi $ABCD$, ta có $AC \perp BD$.\\ Do đó $IJ \perp BD$, nên góc giữa chúng bằng $90^\circ$.''')
            list_th_2 = [loigiai_th_1]

            # Kết hợp và xáo trộn
            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ########################################################################
            # Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = r'\True Góc giữa hai đường thẳng $IJ$ và $MN$ là $60^\circ$'
            vd_da_1_s = r'Góc giữa hai đường thẳng $IJ$ và $MN$ là $30^\circ$'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = (r'''Ta có $IJ \parallel AC$ và $MN \parallel AB$. \\ Góc giữa $IJ$ và $MN$ bằng góc giữa $AC$ và $AB$.\\ Vì $\widehat{ABC} = 180^\circ - 120^\circ = 60^\circ$ và $BA=BC$ nên $\triangle ABC$ đều, suy ra $\widehat{BAC} = 60^\circ$.''')
            list_vd_2 = [loigiai_vd_1]

            # Kết hợp và xáo trộn
            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ########################################################################
            # Vận dụng cao ############################################
            # Các đáp án
            goc_approx = round(float(deg(acos(1/4))), 1)
            vdc_da_1_d = r'\True Góc giữa hai đường thẳng $MN$ và $SC$ xấp xỉ $%s^\circ$' % (str(goc_approx).replace('.', ','))
            vdc_da_1_s = r'Góc giữa hai đường thẳng $MN$ và $SC$ là $45^\circ$'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = (r'''Ta có $MN \parallel AB$. Gọi $\phi$ là góc giữa $AB$ và $SC$.\\ Ta có $\vec{AB} \cdot \vec{SC} = \vec{AB}(\vec{AC}-\vec{AS}) = \vec{AB}\cdot\vec{AC} - 0 = a \cdot a \cdot \cos 60^\circ = \frac{a^2}{2}$. \\ Độ dài $SC = \sqrt{SA^2+AC^2} = \sqrt{3a^2+a^2} = 2a$. \\ Khi đó $\cos \phi = \frac{a^2/2}{a \cdot 2a} = \frac{1}{4} \Rightarrow \phi \approx %s^\circ$.''' % (str(goc_approx).replace('.', ',')))
            list_vdc_2 = [loigiai_vdc_1]

            # Kết hợp và xáo trộn
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))
            random.shuffle(combined_vdc)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

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
                    # Cập nhật lại các biến để xuất kết quả
                    final_ans = answers
                    break

            # Gán lại vào list để giữ đúng cấu trúc template
            shuffled_answers_nb = [final_ans[0]]
            shuffled_answers_th = [final_ans[1]]
            shuffled_answers_vd = [final_ans[2]]
            shuffled_answers_vdc = [final_ans[3]]

            # Xuất nội dung theo định dạng yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' +
                str(noidungcauhoi) + 
                '\n\\choiceTFn \n'
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

